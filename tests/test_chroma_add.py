from vector_db.vector_db_manager import VectorDBManager
from embeddings.embedding_manager import EmbeddingManager

# Initialize
vector_db = VectorDBManager().get_vector_db()
embedder = EmbeddingManager().get_embedder()

text = """
def login():
    print("Hello")
"""

embedding = embedder.embed_text(text)

vector_db.add_documents(
    ids=["test_chunk_1"],
    embeddings=[embedding],
    documents=[text],
    metadatas=[
        {
            "path": "app.py",
            "type": "function",
            "name": "login"
        }
    ]
)

print("✅ Document stored successfully!")