from vector_db.chroma_db import ChromaDB

if __name__ == "__main__":

    db = ChromaDB()

    current_ids = {
        r"data\repositories\flask\README.md_chunk_2",
        r"data\repositories\flask\README.md_chunk_3",
    }

    deleted = db.delete_missing_chunks(current_ids)

    print(f"Deleted {deleted} stale chunks.")
