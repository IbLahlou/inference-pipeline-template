# {{cookiecutter.project_slug}}

This project contains a BentoML service for a {{cookiecutter.model_framework}} model named {{cookiecutter.model_name}} capable of {{cookiecutter.batchable}} batch processing.

## Installation
Install the necessary dependencies:

```bash
pip install -r service/requirements.txt
```

## Running the Service
Run the BentoML service:

```bash
bentoml serve {{cookiecutter.model_service_name}}:
```
