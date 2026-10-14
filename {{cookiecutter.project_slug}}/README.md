# {{ cookiecutter.project_slug }}

BentoML inference service for `{{ cookiecutter.model_name }}` ({{ cookiecutter.model_framework }}).

## Quickstart

```bash
# Install dependencies
pip install -r requirements.txt

# Save the placeholder model to BentoML store
python models.py

# Run the service locally
bentoml serve {{ cookiecutter.model_service_name }}:svc
```

## Docker

```bash
# Build and run
docker compose up --build

# With monitoring (Prometheus + Grafana)
docker compose --profile monitoring up --build
```

## API endpoints

| Endpoint   | Method | Description              |
|------------|--------|--------------------------|
| `/health`  | POST   | Liveness check           |
| `/ready`   | POST   | Readiness check          |
| `/predict` | POST   | Run model inference      |
| `/metrics` | POST   | Prometheus-format metrics|
| `/version` | POST   | Service and model version|

## Example request

```bash
curl -X POST http://localhost:{{ cookiecutter.api_port }}/predict \
  -H "Content-Type: application/json" \
  -d '[[1.0, 2.0, 3.0, 4.0]]'
```

## Tests

```bash
pip install pytest
pytest tests/ -v
```
