import chromadb
from utils.config import CHROMA_DB_PATH, COLLECTION_NAME
from vector_db.base_vector_db import BaseVectorDB

class ChromaDB(BaseVectorDB):

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=CHROMA_DB_PATH
        )

        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME
        )

    def add_documents(self, ids, embeddings, documents, metadatas):
        self.collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas
        )

    def search(self, query_embedding, top_k=5):
        results = self.collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
        )

        return results

    def document_exists(self, document_id):

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
    
    def delete_collection(self):
        pass