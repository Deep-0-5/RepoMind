from processing.chunkers.generic_chunker import GenericChunker
from processing.chunkers.python_chunker import PythonChunker


class ChunkManager:
    """Chooses the correct chunker for each file type."""

    def __init__(self):
        self.python_chunker = PythonChunker()
        self.generic_chunker = GenericChunker()

    def get_chunker(self, extension):
        if extension == ".py":
            return self.python_chunker

        return self.generic_chunker