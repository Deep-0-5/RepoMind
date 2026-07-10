from vector_db.chroma_db import ChromaDB

if __name__ == "__main__":

    db = ChromaDB()

    print(db.document_exists("app.py_chunk_1"))
    print(db.document_exists("random_chunk"))
