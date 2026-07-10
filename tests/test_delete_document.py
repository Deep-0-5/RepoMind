from vector_db.chroma_db import ChromaDB

if __name__ == "__main__":

    db = ChromaDB()

    doc_id = r"data\repositories\flask\examples\celery\src\task_app\views.py_chunk_1"

    print("Before delete:")
    print(db.document_exists(doc_id))

    db.delete_documents([doc_id])

    print()

    print("After delete:")
    print(db.document_exists(doc_id))
