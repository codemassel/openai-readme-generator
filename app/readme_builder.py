from logging_config import logger
from cache_manager import CacheManager

class ReadmeBuilder:
    def __init__(self, generator):
        self.generator = generator
        self.cache = CacheManager()

    def build_readme(self, repo_info: dict) -> str:
        """
        Baut das komplette README, prüft zuerst den Cache
        """
        repo_full_name = f"{repo_info.get('name')}"
        cached = self.cache.get(repo_full_name)
        if cached:
            logger.info(f"README aus Cache geladen für Repo {repo_full_name}")
            return cached

        try:
            readme_text = self.generator.generate_full_readme(repo_info)
            self.cache.set(repo_full_name, readme_text)
            return readme_text
        except Exception as e:
            logger.error(f"Fehler beim Zusammenbauen des READMEs: {e}")
            return f"Error building README: {e}"
