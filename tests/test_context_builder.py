from rag.context_builder import ContextBuilder


SAMPLE_CHUNKS = [
    {
        "path": "app.py",
        "type": "function",
        "name": "login",
        "score": 0.1234,
        "content": "def login():\n    pass",
    },
    {
        "path": "models/user.py",
        "type": "class",
        "name": "User",
        "score": 0.5678,
        "content": "class User:\n    pass",
    },
]


def test_build_context_includes_every_chunk():
    builder = ContextBuilder()

    context = builder.build_context(SAMPLE_CHUNKS)

    assert "app.py" in context
    assert "models/user.py" in context
    assert "login" in context
    assert "User" in context


def test_build_context_formats_score_to_four_decimals():
    builder = ContextBuilder()

    context = builder.build_context(SAMPLE_CHUNKS)

    assert "0.1234" in context
    assert "0.5678" in context


def test_build_context_on_empty_list_still_has_a_header():
    builder = ContextBuilder()

    context = builder.build_context([])

    assert "Repository Context" in context
