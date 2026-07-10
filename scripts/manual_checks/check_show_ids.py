from vector_db.chroma_db import ChromaDB

db = ChromaDB()

results = db.collection.get()

print(f"Total IDs: {len(results['ids'])}")

print("\nFirst 20 IDs:\n")

for doc_id in results["ids"][:20]:
    print(doc_id)