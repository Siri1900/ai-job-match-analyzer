# AI Job Match Analyzer

SKILLS = [
    "python",
    "sql",
    "machine learning",
    "artificial intelligence",
    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "aws",
    "azure",
    "gcp",
    "docker",
    "kubernetes",
    "git",
    "fastapi",
    "langchain",
    "rag"
]


def find_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return found_skills
test_text = """
We are looking for a Python developer with experience in
SQL, AWS, Docker, Kubernetes and FastAPI.
"""

print(find_skills(test_text))