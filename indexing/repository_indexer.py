from repository.parser import RepositoryParser
from repository.file_reader import FileReader

from processing.chunkers.chunk_manager import ChunkManager

from embeddings.embedding_manager import EmbeddingManager

from vector_db.vector_db_manager import VectorDBManager

from utils.logger import setup_logger


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

        logger.info("Repository indexing started.")

        # Parse repository
        files = self.parser.parse_repository(repository_path)

        # Load already indexed chunk IDs
        existing_ids = self.vector_db.get_all_ids()

        logger.info(
            f"Loaded {len(existing_ids)} existing chunks."
        )

        logger.info(
            f"Found {len(files)} supported files."
        )

        total_chunks = 0

        for file in files:

            content = self.reader.read_file(file["path"])

            if not content:
                continue

            chunker = self.chunk_manager.get_chunker(
                file["extension"]
            )

            chunks = chunker.chunk(content, file)

            logger.info(
                f"{file['path']} -> {len(chunks)} chunks"
            )

            ids = []
            embeddings = []
            documents = []
            metadatas = []

            for chunk in chunks:

                chunk_id = (
                    f"{file['path']}_chunk_{chunk.chunk_id}"
                )

                # Skip already indexed chunks
                if chunk_id in existing_ids:

                    logger.info(
                        f"Skipping {chunk_id} (already indexed)"
                    )

                    continue

                try:

                    embedding = self.embedder.embed_text(
                        chunk.content
                    )

                except Exception as e:

                    logger.error(
                        f"Embedding failed for {chunk_id}: {e}"
                    )

                    continue

                if embedding is None:
                    continue

                ids.append(chunk_id)

                embeddings.append(embedding)

                documents.append(chunk.content)

                metadatas.append(
                    chunk.to_metadata()
                )

            if ids:

                self.vector_db.add_documents(
                    ids=ids,
                    embeddings=embeddings,
                    documents=documents,
                    metadatas=metadatas
                )

                total_chunks += len(ids)

                logger.info(
                    f"Stored {len(ids)} new chunks."
                )

            else:

                logger.info(
                    "No new chunks to store."
                )

        logger.info(
            f"Repository indexing completed. Total new indexed chunks: {total_chunks}"
        )

        return total_chunks