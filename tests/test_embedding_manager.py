from embeddings.embedding_manager import EmbeddingManager

if __name__ == "__main__":

    embedder = EmbeddingManager().get_embedder()

    print(type(embedder).__name__)
