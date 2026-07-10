from vector_db.chroma_db import ChromaDB

db = ChromaDB()

# Edit this to a chunk_id that actually exists in your indexed data --
# run check_show_ids.py first to see real IDs.
doc_id = "data/repositories/flask/examples/celery/src/task_app/views.py_chunk_1"

print("Before delete:")
print(db.document_exists(doc_id))

db.delete_documents([doc_id])

print()

print("After delete:")
print(db.document_exists(doc_id))