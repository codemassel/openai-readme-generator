from github_client import GitHubClient

def test_get_repo_info():
    client = GitHubClient()
    info = client.get_repo_info("octocat", "Hello-World")
    assert "name" in info
    assert "description" in info
