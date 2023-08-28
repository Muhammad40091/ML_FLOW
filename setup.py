import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "ML_FLOW"
AUTHOR_USER_NAME = "Muhammad40091"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "muhammadabbas40091@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package with mlapps",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Corrected argument name
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug_Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},  # Corrected package_dir argument
    packages=setuptools.find_packages(where="src"),
)
