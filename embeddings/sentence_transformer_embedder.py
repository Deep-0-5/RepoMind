from embeddings.base_embedder import BaseEmbedder

from utils.ApplicationResources import ResourceManager


class SentenceTransformerEmbedder(BaseEmbedder):
    """
    Local embedding provider using Sentence Transformers.
    """

    def __init__(self):

        self.model = (
            ResourceManager.get_sentence_transformer()
        )

    def embed_text(self, text: str) -> list[float]:

        if not text.strip():
            raise ValueError(
                "Input text cannot be empty."
            )

        embedding = self.model.encode(
            text,
            normalize_embeddings=True
        )

        return embedding.tolist()

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """
        Embed multiple texts at once using Sentence Transformers.
        Much faster than calling embed_text() in a loop due to
        batched GPU/CPU operations.
        """

        if not texts:
            return []

        cleaned = [t if t.strip() else " " for t in texts]

        embeddings = self.model.encode(
            cleaned,
            normalize_embeddings=True,
            batch_size=64
        )

        return [e.tolist() for e in embeddings]