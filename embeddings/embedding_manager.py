from embeddings.gemini_embedder import GeminiEmbedder
from embeddings.sentence_transformer_embedder import (
    SentenceTransformerEmbedder
)

from utils.config import EMBEDDING_PROVIDER

from utils.logger import setup_logger


logger = setup_logger(__name__)


class EmbeddingManager:
    """
    Returns the configured embedding provider.
    """

    def __init__(self):

        provider = EMBEDDING_PROVIDER.lower()

        if provider == "gemini":

            logger.info(
                "Using Gemini Embedder"
            )

            self.embedder = GeminiEmbedder()

        elif provider == "sentence_transformer":

            logger.info(
                "Using Sentence Transformer Embedder"
            )

            self.embedder = SentenceTransformerEmbedder()

        else:

            raise ValueError(
                f"Unsupported embedding provider: {provider}"
            )

    def get_embedder(self):

        return self.embedder