from openai import OpenAI
from config import OPENAI_API_KEY
from logging_config import logger

class AIReadmeGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate_full_readme(self, repo_info: dict) -> str:
        """
        Generiert das komplette README auf einmal (Description, Installation, Usage, License)
        """
        prompt = f"""
        Schreibe ein komplettes README für ein GitHub-Projekt basierend auf diesen Infos:
        {repo_info}
        Sektionen: Description, Installation, Usage, License
        Bitte formatiere als Markdown mit Überschriften (# Description, # Installation, etc.)
        """
        try:
            logger.info(f"Generiere komplettes README für Repo {repo_info.get('name')}")
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1200
            )
            readme_text = response.choices[0].message.content.strip()
            logger.info("README erfolgreich generiert")
            return readme_text
        except Exception as e:
            logger.error(f"Fehler bei der Generierung des READMEs: {e}")
            return f"Error generating README: {e}"
