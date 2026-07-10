from utils.config import COLLECTION_NAME
from utils.ApplicationResources import ResourceManager

from vector_db.base_vector_db import BaseVectorDB


class ChromaDB(BaseVectorDB):

    def __init__(self):

        self.client = (
            ResourceManager.get_chroma_client()
        )

        self.collection = (
            ResourceManager.get_chroma_collection()
        )

    def add_documents(
        self,
        ids,
        embeddings,
        documents,
        metadatas
    ):

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )

    def delete_documents(self, ids):
        """
        Delete documents by their IDs.
        """

        self.collection.delete(
            ids=ids
        )

    def search(
        self,
        query_embedding,
        top_k=5
    ):

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results

    def document_exists(
        self,
        document_id
    ):

        result = self.collection.get(
            ids=[document_id]
        )

        return len(result["ids"]) > 0

    def get_all_ids(self):
        """
        Returns all indexed document IDs.
        """

        results = self.collection.get()

        return set(results["ids"])

    def delete_missing_chunks(
        self,
        current_chunk_ids
    ):
        """
        Deletes chunks that are no longer present
        in the repository.
        """

        stored_ids = self.get_all_ids()

        stale_ids = list(
            stored_ids - current_chunk_ids
        )

        if stale_ids:

            self.delete_documents(
                stale_ids
            )

        return len(stale_ids)

    def get_existing_chunks(self):
        """
        Returns a dictionary mapping
        document ID -> stored hash.
        """

        results = self.collection.get()

        existing_chunks = {}

        ids = results["ids"]
        metadatas = results["metadatas"]

        for doc_id, metadata in zip(
            ids,
            metadatas
        ):

            existing_chunks[doc_id] = (
                metadata.get("hash")
            )

        return existing_chunks

    def delete_collection(self):

        self.client.delete_collection(
            COLLECTION_NAME
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=COLLECTION_NAME
            )
        )