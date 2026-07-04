from repository.file_reader import FileReader

reader = FileReader()

content = reader.read_file("data/repositories/flask/README.md")

print(content[:500])