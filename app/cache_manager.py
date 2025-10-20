import json
import os
from logging_config import logger

CACHE_FILE = "cache.json"

class CacheManager:
    def __init__(self):
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                self.cache = json.load(f)
        else:
            self.cache = {}

    def get(self, repo_full_name: str):
        return self.cache.get(repo_full_name)

    def set(self, repo_full_name: str, readme_text: str):
        self.cache[repo_full_name] = readme_text
        self._save()

    def _save(self):
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(self.cache, f, indent=2, ensure_ascii=False)
        logger.info(f"Cache gespeichert: {CACHE_FILE}")
