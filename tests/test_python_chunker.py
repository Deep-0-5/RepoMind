from processing.chunkers.python_chunker import PythonChunker


CODE = """
def login():
    print("Login")

class User:
    def greet(self):
        print("hi")

def logout():
    print("Logout")
"""

METADATA = {"path": "app.py", "extension": ".py", "size": len(CODE)}


def test_extracts_one_chunk_per_top_level_function_or_class():
    chunker = PythonChunker()

    chunks = chunker.chunk(CODE, METADATA)

    names = [c.name for c in chunks]

    assert names == ["login", "User", "logout"]


def test_chunk_types_are_classified_correctly():
    chunker = PythonChunker()

    chunks = chunker.chunk(CODE, METADATA)

    types = {c.name: c.type for c in chunks}

    assert types["login"] == "function"
    assert types["User"] == "class"
    assert types["logout"] == "function"


def test_chunk_content_contains_the_original_source():
    chunker = PythonChunker()

    chunks = chunker.chunk(CODE, METADATA)

    login_chunk = next(c for c in chunks if c.name == "login")

    assert "def login()" in login_chunk.content
    assert 'print("Login")' in login_chunk.content


def test_nested_methods_are_not_extracted_as_top_level_chunks():
    chunker = PythonChunker()

    chunks = chunker.chunk(CODE, METADATA)

    # `greet` is a method inside User, not a top-level node --
    # it should not appear as its own chunk.
    names = [c.name for c in chunks]

    assert "greet" not in names
