from processing.chunkers.base_chunker import BaseChunker
from models.chunk import Chunk
from utils.hash_utils import generate_hash


class GenericChunker(BaseChunker):
    """Fallback line-aware chunker for unsupported languages."""

    def __init__(self, chunk_size=1000, overlap=200):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(self, text, metadata):
        if not text:
            return []

        lines = text.splitlines(keepends=True)
        chunks = []
        chunk_id = 1

        # Precompute character spans for each line
        line_spans = []
        current_offset = 0
        for line in lines:
            line_len = len(line)
            line_spans.append((line, current_offset, current_offset + line_len))
            current_offset += line_len

        start_line_idx = 0
        total_lines = len(line_spans)

        while start_line_idx < total_lines:
            chunk_content_parts = []
            chunk_char_count = 0
            chunk_start_char = line_spans[start_line_idx][1]
            chunk_end_char = chunk_start_char

            curr_idx = start_line_idx
            while curr_idx < total_lines and chunk_char_count < self.chunk_size:
                line_text, _, end_char = line_spans[curr_idx]
                chunk_content_parts.append(line_text)
                chunk_char_count += len(line_text)
                chunk_end_char = end_char
                curr_idx += 1

            chunk_content = "".join(chunk_content_parts)
            chunk = Chunk(
                chunk_id=chunk_id,
                content=chunk_content,
                path=metadata["path"],
                extension=metadata["extension"],
                start_char=chunk_start_char,
                end_char=chunk_end_char,
                hash=generate_hash(chunk_content)
            )
            chunks.append(chunk)
            chunk_id += 1

            if curr_idx >= total_lines:
                break

            # Find the next starting line by backtracking to satisfy overlap
            backtrack_chars = 0
            next_start_idx = curr_idx - 1
            while next_start_idx > start_line_idx:
                line_len = len(line_spans[next_start_idx][0])
                if backtrack_chars + line_len > self.overlap:
                    break
                backtrack_chars += line_len
                next_start_idx -= 1

            # Make sure we always make progress
            if next_start_idx <= start_line_idx:
                start_line_idx = curr_idx
            else:
                start_line_idx = next_start_idx + 1

        return chunks