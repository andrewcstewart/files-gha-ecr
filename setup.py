from setuptools import setup, find_packages

setup(
    name="files-gha-ecr",
    version="0.1",
    description="Meltano project files for Amazon ECR CI/CD via Github Action",
    packages=find_packages(),
    package_data={
        "bundle": [
            ".github/workflows/ecr.yml",         
        ]
    },
)
