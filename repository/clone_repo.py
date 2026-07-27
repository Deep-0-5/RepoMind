from urllib.parse import urlparse
from git import Repo, GitCommandError
from pathlib import Path
from utils.logger import setup_logger

logger = setup_logger(__name__)


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

        destination.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if destination.exists():
            logger.info("Repository already exists.")
            return True

        try:
            logger.info(f"Cloning {url} to {destination}...")
            Repo.clone_from(url, destination)
            logger.info("Repository cloned successfully!")
            return True

        except GitCommandError as e:
            logger.error(f"Git Error cloning {url}: {e}")
            return False