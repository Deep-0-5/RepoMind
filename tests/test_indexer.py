from indexing.repository_indexer import RepositoryIndexer

indexer = RepositoryIndexer()

total = indexer.index_repository(
    "data/repositories/flask"
)

print(f"\nRepository Indexed Successfully!")
print(f"Total Chunks Indexed: {total}")