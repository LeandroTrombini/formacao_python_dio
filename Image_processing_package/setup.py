from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_project_test",
    version="0.0.2",
    author="leandro_trombini",
    author_email="leandro_trombini@gmail.com",
    description="Package description",
    long_description=page_description,
    long_description_conten_type="text/markdown",
    url="https://github.com/leandrotrombini",
    packages=find_packages(), 
    install_requires=requirements,
    python_requires='>=3.8',
)
