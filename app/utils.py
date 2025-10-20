import re

def sanitize_text(text: str) -> str:
    """Bereinigt Text von unerwünschten Whitespaces und Zeichen"""
    return text.strip().replace("\r\n", "\n")

def validate_github_input(owner: str, repo_name: str) -> bool:
    """
    Prüft, ob Owner und Repo-Name nur erlaubte Zeichen enthalten
    """
    pattern = r'^[\w-]+$'
    return bool(re.match(pattern, owner) and re.match(pattern, repo_name))
