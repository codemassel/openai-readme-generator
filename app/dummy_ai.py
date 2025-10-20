from logging_config import logger

class DummyAI:
    """
    Mock/Platzhalter AI-Generator zum Testen ohne OpenAI API.
    """
    def generate_full_readme(self, repo_info: dict) -> str:
        logger.info(f"[DummyAI] Generiere Dummy README für Repo {repo_info.get('name')}")
        return f"""# Description
Dies ist ein Dummy-README für {repo_info.get('name')}

# Installation
Keine Installation nötig

# Usage
Einfach ausführen

# License
MIT"""
