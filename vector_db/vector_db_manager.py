from vector_db.chroma_db import ChromaDB


class VectorDBManager:

    def __init__(self):
        self.vector_db = ChromaDB()

    def get_vector_db(self):
        return self.vector_db