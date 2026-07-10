from embeddings.embedding_manager import EmbeddingManager

embedder = EmbeddingManager().get_embedder()

print(type(embedder).__name__)