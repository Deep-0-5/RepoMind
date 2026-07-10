from indexing.repository_indexer import RepositoryIndexer

if __name__ == "__main__":

    indexer = RepositoryIndexer()

    total = indexer.index_repository(
        "data/repositories/flask"
    )

    print(f"\nRepository Indexed Successfully!")
    print(f"Total Chunks Indexed: {total}")
