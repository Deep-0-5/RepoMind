from embeddings.embedding_manager import EmbeddingManager
from vector_db.vector_db_manager import VectorDBManager


class Retriever:
    """
    Retrieves the most relevant code chunks from the vector database.
    """

    def __init__(self):
        self.embedder = EmbeddingManager().get_embedder()
        self.vector_db = VectorDBManager().get_vector_db()

    def retrieve(
        self,
        question: str,
        top_k: int = 5,
        max_distance: float = 1.0
    ):
        """
        Retrieve relevant chunks for a question.

        Args:
            question: The search query.
            top_k: Maximum number of results to return.
            max_distance: Maximum L2 distance threshold.
                          Chunks above this are filtered out.
        """

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

            # Filter out low-quality matches
            if distance > max_distance:
                continue

            retrieved_chunks.append(
                {
                    "content": document,
                    "path": metadata.get("path"),
                    "type": metadata.get("type"),
                    "name": metadata.get("name"),
                    "extension": metadata.get("extension"),
                    "score": distance
                }
            )

        return retrieved_chunks