from vector_db.vector_db_manager import VectorDBManager
from embeddings.embedding_manager import EmbeddingManager

if __name__ == "__main__":

    # Initialize managers
    vector_db = VectorDBManager().get_vector_db()
    embedder = EmbeddingManager().get_embedder()

    # User query
    query = "How do users login?"

    # Convert query to embedding
    query_embedding = embedder.embed_text(query)

    # Search in ChromaDB
    results = vector_db.search(query_embedding)

    # Pretty print the results
    for doc, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        print("=" * 50)
        print(f"Score: {distance:.4f}")
        print(f"File: {metadata['path']}")
        print(f"Type: {metadata.get('type')}")
        print(doc)
