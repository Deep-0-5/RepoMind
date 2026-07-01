from urllib.parse import urlparse
from git import Repo, GitCommandError
from pathlib import Path

class RepositoryCloner:
    """Handles cloning GitHub repositories."""

    def __init__(self):
        pass

    def validate_url(self, url):
        parsed_url = urlparse(url)
        
        if parsed_url.scheme != "https":
            return False
        
        if parsed_url.netloc != "github.com":
            return False
        
        path_parts = parsed_url.path.strip("/").split("/")
        
        if len(path_parts) < 2:
            return False
        
        return True
        
        

    def get_repo_name(self, url):
        parsed_url = urlparse(url)
        
        path_parts = parsed_url.path.strip("/").split("/")
        repo_name = path_parts[1]
        
        if repo_name.endswith(".git"):
            repo_name = repo_name[:-4]

        return repo_name
        
    def clone_repository(self, url):
        repo_name = self.get_repo_name(url)

        destination = Path("data") / "repositories" / repo_name

        if destination.exists():
            print("Repository already exists.")
            return True

        try:
            Repo.clone_from(url, destination)
            print("Repository cloned successfully!")
            return True

        except GitCommandError as e:
            print(f"Git Error: {e}")
            return False    