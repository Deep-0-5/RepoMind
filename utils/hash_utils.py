import hashlib

def generate_hash(text: str) -> str:
    """
    Generate SHA256 hash for a chunk.
    """

    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()