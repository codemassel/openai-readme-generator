from github_client import GitHubClient
from readme_builder import ReadmeBuilder
from utils import validate_github_input

# wenn True = Dummy wird genutzt um OPENAI-API zu entlasten
USE_DUMMY = True

if USE_DUMMY:
    from dummy_ai import DummyAI as AIClass
else:
    from ai_generator import AIReadmeGenerator as AIClass


def main():
    owner = input("GitHub Owner: ")
    repo_name = input("Repo Name: ")

    if not validate_github_input(owner, repo_name):
        print("Ungültiger Owner oder Repo-Name! Nur Buchstaben, Zahlen, _ und - erlaubt.")
        return

    github_client = GitHubClient()
    repo_info = github_client.get_repo_info(owner, repo_name)

    ai_gen = AIClass()
    builder = ReadmeBuilder(ai_gen)

    readme = builder.build_readme(repo_info)

    with open("GENERATED_README.md", "w", encoding="utf-8") as f:
        f.write(readme)

    print("✅ README erfolgreich generiert! Datei: GENERATED_README.md")


if __name__ == "__main__":
    main()
