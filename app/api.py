from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from github_client import GitHubClient
from readme_builder import ReadmeBuilder
from dummy_ai import DummyAI  # Standardmäßig DummyAI
from utils import validate_github_input

app = FastAPI(title="README Generator API")

class RepoRequest(BaseModel):
    owner: str
    repo_name: str

# wenn True = Dummy wird genutzt um OPENAI-API zu entlasten
USE_DUMMY = True
AIClass = DummyAI

@app.post("/generate-readme")
def generate_readme(req: RepoRequest):
    if not validate_github_input(req.owner, req.repo_name):
        raise HTTPException(status_code=400, detail="Ungültiger Owner oder Repo-Name")

    github_client = GitHubClient()
    repo_info = github_client.get_repo_info(req.owner, req.repo_name)

    ai_gen = AIClass()
    builder = ReadmeBuilder(ai_gen)

    readme_text = builder.build_readme(repo_info)
    return {"readme": readme_text}
