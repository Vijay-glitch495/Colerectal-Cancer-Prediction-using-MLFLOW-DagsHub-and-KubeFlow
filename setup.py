from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Colerectal_Cancer_Prediction",
    version="0.1",
    author="Vijay Kumar Reddy Bommireddy",
    packages=find_packages(),
    install_requires = requirements,
)