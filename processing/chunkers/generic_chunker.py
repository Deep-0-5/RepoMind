from processing.chunkers.base_chunker import BaseChunker
from models.chunk import Chunk

class GenericChunker(BaseChunker):
    """Fallback chunker for unsupported languages."""

    def __init__(self, chunk_size=1000, overlap=200):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text, metadata):
        chunks = []

        start = 0
        chunk_id = 1

        while start < len(text):

            end = min(start + self.chunk_size, len(text))

            chunk = Chunk(
                chunk_id=chunk_id,
                content=text[start:end],
                path=metadata["path"],
                extension=metadata["extension"],
                start_char=start,
                end_char=end
            )

            chunks.append(chunk)

            start += self.chunk_size - self.overlap
            chunk_id += 1

        return chunks