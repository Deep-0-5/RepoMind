# vector_db/base_vector_db.py

from abc import ABC, abstractmethod


class BaseVectorDB(ABC):

    @abstractmethod
    def add_documents(self, ids, embeddings, documents, metadatas):
        pass

    @abstractmethod
    def search(self, query_embedding, top_k=5):
        pass

    @abstractmethod
    def delete_collection(self):
        pass