from vector_db.chroma_db import ChromaDB

# DESTRUCTIVE: this permanently deletes the entire ChromaDB collection.
# Requires typed confirmation so it can never run by accident.
confirmation = input(
    "Type DELETE to permanently wipe the vector database collection: "
)

if confirmation != "DELETE":
    print("Aborted. Nothing was deleted.")
else:
    db = ChromaDB()
    db.delete_collection()
    print("Collection deleted successfully.")