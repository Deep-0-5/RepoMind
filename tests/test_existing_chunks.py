from vector_db.chroma_db import ChromaDB

if __name__ == "__main__":

    db = ChromaDB()

    chunks = db.get_existing_chunks()

    print(f"Total Indexed Chunks: {len(chunks)}")

    print()

    for chunk_id, chunk_hash in list(chunks.items())[:5]:

        print(chunk_id)

        print(chunk_hash)

        print("-" * 60)
