from ai_generator import AIReadmeGenerator

def test_generate_section():
    ai = AIReadmeGenerator()
    dummy_repo = {"name": "Test", "description": "Dummy"}
    section_text = ai.generate_readme_section(dummy_repo, "Description")
    assert isinstance(section_text, str)
    assert len(section_text) > 0
