from processing.chunkers.chunk_manager import ChunkManager

manager = ChunkManager()

print(type(manager.get_chunker(".py")).__name__)
print(type(manager.get_chunker(".js")).__name__)
print(type(manager.get_chunker(".java")).__name__)