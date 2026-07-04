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