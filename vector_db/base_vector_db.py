# vector_db/base_vector_db.py

from abc import ABC, abstractmethod


class BaseVectorDB(ABC):

    @abstractmethod
    def add_documents(self, ids, embeddings, documents, metadatas):
        pass

    @abstractmethod
    def delete_documents(self, ids):
        pass

    @abstractmethod
    def search(self, query_embedding, top_k=5):
        pass

    @abstractmethod
    def document_exists(self, document_id):
        pass

    @abstractmethod
    def get_all_ids(self):
        pass

    @abstractmethod
    def delete_missing_chunks(self, current_chunk_ids):
        pass

    @abstractmethod
    def get_existing_chunks(self):
        pass

    @abstractmethod
    def delete_collection(self):
        pass