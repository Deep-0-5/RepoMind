from embeddings.sentence_transformer_embedder import (

if __name__ == "__main__":
        SentenceTransformerEmbedder
    )

    embedder = SentenceTransformerEmbedder()

    embedding = embedder.embed_text(
        "Hello World"
    )

    print(type(embedding))
    print(len(embedding))
    print(embedding[:10])
