from github import Github
from config import GITHUB_TOKEN
from logging_config import logger

class GitHubClient:
    def __init__(self):
        self.client = Github(GITHUB_TOKEN)

    def get_repo_info(self, owner: str, repo_name: str) -> dict:
        try:
            logger.info(f"Hole Repo-Infos für {owner}/{repo_name}")
            repo = self.client.get_repo(f"{owner}/{repo_name}")
            info = {
                "name": repo.name,
                "description": repo.description,
                "stars": repo.stargazers_count,
                "forks": repo.forks_count,
                "language": repo.language,
                "issues": repo.open_issues_count,
                "url": repo.html_url
            }
            logger.info(f"Repo-Infos erfolgreich abgerufen: {info['name']}")
            return info
        except Exception as e:
            logger.error(f"Fehler beim Abrufen von Repo-Infos: {e}")
            return {}
