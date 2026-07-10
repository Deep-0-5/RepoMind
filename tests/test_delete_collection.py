from vector_db.chroma_db import ChromaDB

if __name__ == "__main__":

    db = ChromaDB()

    db.delete_collection()

    print("Collection deleted successfully.")
