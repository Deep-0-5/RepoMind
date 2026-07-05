from embeddings.embedding_manager import EmbeddingManager
from vector_db.vector_db_manager import VectorDBManager


class Retriever:
    """
    Retrieves the most relevant code chunks from the vector database.
    """

    def __init__(self):
        self.embedder = EmbeddingManager().get_embedder()
        self.vector_db = VectorDBManager().get_vector_db()

    def retrieve(self, question: str, top_k: int = 5):

        if not question.strip():
            raise ValueError("Question cannot be empty.")

        query_embedding = self.embedder.embed_text(question)

        results = self.vector_db.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        retrieved_chunks = []

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]
        distances = results["distances"][0]

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances
        ):

            retrieved_chunks.append(
                {
                    "content": document,
                    "path": metadata.get("path"),
                    "type": metadata.get("type"),
                    "name": metadata.get("name"),
                    "score": distance
                }
            )

        return retrieved_chunks