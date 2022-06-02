# files-gha-ecr
Meltano project file bundle for Github Actions CI/CD that publishes to Amazon ECR 

This plugin will add the following files to your Meltano project:

- `.github/workflows/ecr.yml`

## Installation

To install the Gitpod file bundle into your Meltano project you need to use a custom file bundle. This file bundle builds on top of the Docker file bundle.

```
# Add Docker files to your Meltano project
meltano add files docker

# Add Gitpod files to your Meltano project
meltano add --custom files gitpod
```
