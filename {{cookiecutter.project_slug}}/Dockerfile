# ---------- builder ----------
FROM python:3.11-slim AS builder

WORKDIR /build

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# ---------- runtime ----------
FROM python:3.11-slim

RUN groupadd -r appuser && useradd -r -g appuser -d /app -s /sbin/nologin appuser

WORKDIR /app

COPY --from=builder /install /usr/local
COPY . .

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE {{ cookiecutter.api_port }}

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:{{ cookiecutter.api_port }}/health')"

CMD ["bentoml", "serve", "{{ cookiecutter.model_service_name }}:svc", "--port", "{{ cookiecutter.api_port }}"]
