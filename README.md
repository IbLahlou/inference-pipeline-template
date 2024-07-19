# BentoML Inference pipeline Cookiecutter Template

This repository provides a Cookiecutter template for quickly scaffolding a BentoML project. It is designed to handle both PyTorch and TensorFlow models, with options for batch processing and dynamic API configurations.

## Features

- Supports PyTorch and TensorFlow model frameworks.
- Optional batch processing with configurable batch dimensions.
- Includes a conditional runner for enhanced model operations.
- Generates a complete BentoML service with structured directories and necessary files.

## Requirements

- Python 3.6 or higher
- Cookiecutter
- BentoML

## Installation

Before you begin, ensure you have Cookiecutter installed on your system. If not, you can install it using pip:

```bash
pip install cookiecutter
```

## Usage

To generate a new BentoML project using this template, run the following command:

```bash
cookiecutter https://github.com/IbLahlou/inference-pipeline-template
```

You will be prompted to enter details such as the project name, model framework, and other configurations. Once provided, the template will create a new directory with all the necessary files for your BentoML service.

## Structure

The generated project will have the following structure:

```
{{cookiecutter.project_slug}}/
├── tests/
│   ├── __init__.py
│   └── models_test.py
├── workflows/
│   └── ci.yml
├── utils.py
├── models.py
├── {{cookiecutter.model_service_name}}.py
├── bentofile.yml
├── requirements.txt
├── setup.py
└── README.md
```

