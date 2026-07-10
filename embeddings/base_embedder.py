from abc import ABC, abstractmethod


class BaseEmbedder(ABC):
    """Base class for all embedding providers."""

    @abstractmethod
    def embed_text(self, text: str) -> list[float]:
        """
        Generate an embedding vector.

        Args:
            text (str): Input text.

        Returns:
            list[float]: Embedding vector.
        """
        pass

    @abstractmethod
    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        """
        Generate embedding vectors for a batch of texts.

        Args:
            texts (list[str]): List of input texts.

        Returns:
            list[list[float]]: List of embedding vectors.
        """
        pass