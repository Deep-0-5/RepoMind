from embeddings.gemini_embedder import GeminiEmbedder


class EmbeddingManager:
    """Returns the configured embedding provider."""

    def __init__(self):
        self.embedder = GeminiEmbedder()

    def get_embedder(self):
        return self.embedder