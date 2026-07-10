from processing.chunkers.chunk_manager import ChunkManager
from processing.chunkers.python_chunker import PythonChunker
from processing.chunkers.generic_chunker import GenericChunker


def test_python_files_get_the_python_chunker():
    manager = ChunkManager()

    assert isinstance(manager.get_chunker(".py"), PythonChunker)


def test_unknown_extensions_get_the_generic_chunker():
    manager = ChunkManager()

    assert isinstance(manager.get_chunker(".js"), GenericChunker)
    assert isinstance(manager.get_chunker(".java"), GenericChunker)
