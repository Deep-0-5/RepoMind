import chromadb

from vector_db.base_vector_db import BaseVectorDB


class ChromaDB(BaseVectorDB):

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="data/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="repository_chunks"
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

    def delete_collection(self):
        pass