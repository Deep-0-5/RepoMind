from abc import ABC, abstractmethod

class BaseChunker(ABC):
    """Base class for all chunkers."""

    @abstractmethod
    def chunk(self, text, metadata):
        """
        Split text into chunks.

        Args:
            text (str): File content.
            metadata (dict): File metadata.

        Returns:
            list: List of chunks.
        """
        pass