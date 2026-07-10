from repository.parser import RepositoryParser
from repository.file_reader import FileReader
from processing.chunkers.chunk_manager import ChunkManager
from embeddings.embedding_manager import EmbeddingManager
from vector_db.vector_db_manager import VectorDBManager
from utils.logger import setup_logger
import time

logger = setup_logger(__name__)


class RepositoryIndexer:
    """Indexes an entire repository into ChromaDB."""

    def __init__(self):
        self.parser = RepositoryParser()
        self.reader = FileReader()
        self.chunk_manager = ChunkManager()
        self.embedder = EmbeddingManager().get_embedder()
        self.vector_db = VectorDBManager().get_vector_db()

    def index_repository(self, repository_path):
        """
        Index a repository and return a stats dict with:
        - files_scanned
        - total_chunks
        - new_chunks
        - updated_chunks
        - skipped_chunks
        - deleted_chunks
        """

        logger.info("Repository indexing started.")
        total_start = time.perf_counter()

        # Parse repository
        parse_start = time.perf_counter()
        files = self.parser.parse_repository(repository_path)
        parse_time = time.perf_counter() - parse_start

        # Load already indexed chunk IDs
        existing_chunks = self.vector_db.get_existing_chunks()

        logger.info(
            f"Loaded {len(existing_chunks)} existing chunks."
        )

        logger.info(
            f"Found {len(files)} supported files."
        )

        total_chunks = 0
        new_chunks = 0
        updated_chunks = 0
        skipped_chunks = 0
        current_chunk_ids = set()
        deleted_chunks = 0
        chunking_time = 0
        embedding_time = 0
        database_time = 0

        for file in files:

            content = self.reader.read_file(file["path"])

            if not content:
                continue

            chunker = self.chunk_manager.get_chunker(
                file["extension"]
            )
            
            chunk_start = time.perf_counter()
            chunks = chunker.chunk(content, file)
            chunking_time += time.perf_counter() - chunk_start

            logger.info(
                f"{file['path']} -> {len(chunks)} chunks"
            )

            # Separate chunks into those that need embedding
            # vs those that can be skipped
            ids_to_store = []
            contents_to_embed = []
            metadatas_to_store = []
            file_new = 0
            file_updated = 0

            for chunk in chunks:

                chunk_id = (
                    f"{file['path']}_chunk_{chunk.chunk_id}"
                )
                
                current_chunk_ids.add(chunk_id)

                stored_hash = existing_chunks.get(chunk_id)

                # New chunk
                if stored_hash is None:
                    file_new += 1

                # Unchanged chunk — skip
                elif stored_hash == chunk.hash:
                    skipped_chunks += 1
                    continue

                # Updated chunk — delete old, re-embed
                else:
                    self.vector_db.delete_documents(
                        [chunk_id]
                    )
                    file_updated += 1

                ids_to_store.append(chunk_id)
                contents_to_embed.append(chunk.content)
                metadatas_to_store.append(
                    chunk.to_metadata()
                )

            if not ids_to_store:
                logger.info(
                    "No new chunks to store."
                )
                continue

            # Batch embed all chunks for this file at once
            try:
                embed_start = time.perf_counter()
                embeddings = self.embedder.embed_batch(
                    contents_to_embed
                )
                embedding_time += (
                    time.perf_counter() - embed_start
                )

            except Exception as e:
                logger.error(
                    f"Batch embedding failed for {file['path']}: {e}"
                )
                continue

            # Filter out any failed embeddings
            valid_ids = []
            valid_embeddings = []
            valid_documents = []
            valid_metadatas = []

            for i, emb in enumerate(embeddings):
                if emb:
                    valid_ids.append(ids_to_store[i])
                    valid_embeddings.append(emb)
                    valid_documents.append(contents_to_embed[i])
                    valid_metadatas.append(metadatas_to_store[i])

            if valid_ids:

                db_start = time.perf_counter()
                self.vector_db.add_documents(
                    ids=valid_ids,
                    embeddings=valid_embeddings,
                    documents=valid_documents,
                    metadatas=valid_metadatas
                )
                database_time += (
                    time.perf_counter() - db_start
                )

                total_chunks += len(valid_ids)
                new_chunks += file_new
                updated_chunks += file_updated

                logger.info(
                    f"Stored {len(valid_ids)} new/updated chunks."
                )

        db_start = time.perf_counter()
        deleted_chunks = self.vector_db.delete_missing_chunks(
            current_chunk_ids
        )
        database_time += (
            time.perf_counter() - db_start
        )
        
        total_time = time.perf_counter() - total_start
        logger.info("=" * 60)
        logger.info("Repository Statistics")
        logger.info("=" * 60)

        logger.info(f"Files Scanned     : {len(files)}")
        logger.info(f"Indexed Chunks    : {total_chunks}")

        logger.info("")

        logger.info(f"New Chunks        : {new_chunks}")
        logger.info(f"Updated Chunks    : {updated_chunks}")
        logger.info(f"Skipped Chunks    : {skipped_chunks}")
        logger.info(f"Deleted Chunks    : {deleted_chunks}")

        logger.info("")

        logger.info(f"Parse Time        : {parse_time:.2f} sec")
        logger.info(f"Chunking Time     : {chunking_time:.2f} sec")
        logger.info(f"Embedding Time    : {embedding_time:.2f} sec")
        logger.info(f"Database Time     : {database_time:.2f} sec")
        logger.info(f"Total Time        : {total_time:.2f} sec")

        logger.info("=" * 60)

        return {
            "files_scanned": len(files),
            "total_chunks": total_chunks,
            "new_chunks": new_chunks,
            "updated_chunks": updated_chunks,
            "skipped_chunks": skipped_chunks,
            "deleted_chunks": deleted_chunks,
        }