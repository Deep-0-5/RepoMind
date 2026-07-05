from processing.chunkers.generic_chunker import GenericChunker

# Create dummy text of 2500 characters
text = "A" * 2500

metadata = {
    "path": "README.md",
    "extension": ".md",
    "size": len(text)
}

chunker = GenericChunker()

chunks = chunker.chunk(text, metadata)

print(f"Total Chunks: {len(chunks)}")

for chunk in chunks:
    print(
        f"Chunk {chunk.chunk_id} | "
        f"Start: {chunk.start_char} | "
        f"End: {chunk.end_char} | "
        f"Length: {len(chunk.content)}"
    )