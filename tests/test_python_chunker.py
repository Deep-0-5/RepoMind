from processing.chunkers.python_chunker import PythonChunker

code = """
def login():
    print("Login")

class User:
    pass

async def fetch_data():
    return []

def logout():
    print("Logout")
"""

metadata = {
    "path": "app.py",
    "extension": ".py"
}

chunker = PythonChunker()

chunks = chunker.chunk(code, metadata)

for chunk in chunks:
    print("=" * 50)
    print(chunk.type)
    print(chunk.name)
    print(chunk.start_line, chunk.end_line)
    print(chunk.content)