from vector_db.chroma_db import ChromaDB

db = ChromaDB()

# Edit these to real chunk_ids you want to KEEP -- everything else
# in the collection will be deleted. Run check_show_ids.py first.
current_ids = {
    "data/repositories/flask/README.md_chunk_2",
    "data/repositories/flask/README.md_chunk_3",
}

deleted = db.delete_missing_chunks(current_ids)

print(f"Deleted {deleted} stale chunks.")