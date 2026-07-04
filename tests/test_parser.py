from repository.parser import RepositoryParser

parser = RepositoryParser()

print(parser.is_supported_file("app.py"))
print(parser.is_supported_file("README.md"))
print(parser.is_supported_file("image.png"))
print(parser.is_supported_file("video.mp4"))