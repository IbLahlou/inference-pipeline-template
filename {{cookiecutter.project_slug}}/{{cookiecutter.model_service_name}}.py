from __future__ import annotations

import json
import logging
import time

import bentoml
import numpy as np
from bentoml.io import JSON, NumpyNdarray, Text

from metrics import REQUEST_LATENCY, PREDICTION_COUNT, ERROR_COUNT, Timer, collect_metrics

__version__ = "0.1.0"

logging.basicConfig(
    format='{"time":"%(asctime)s","level":"%(levelname)s","logger":"%(name)s","message":"%(message)s"}',
    level=logging.INFO,
)
logger = logging.getLogger("{{ cookiecutter.model_service_name }}")

model_runner = bentoml.{{ cookiecutter.model_framework }}.get("{{ cookiecutter.model_name }}:latest").to_runner()

svc = bentoml.Service("{{ cookiecutter.model_service_name }}", runners=[model_runner])

_ready = True


@svc.api(input=Text(), output=JSON(), route="/health")
def health(_: str) -> dict:
    return {"status": "ok"}


@svc.api(input=Text(), output=JSON(), route="/ready")
def ready(_: str) -> dict:
    return {"ready": _ready}


@svc.api(input=Text(), output=Text(), route="/metrics")
def metrics(_: str) -> str:
    return collect_metrics()


@svc.api(input=Text(), output=JSON(), route="/version")
def version(_: str) -> dict:
    return {
        "service": "{{ cookiecutter.model_service_name }}",
        "version": __version__,
        "model": "{{ cookiecutter.model_name }}",
    }


@svc.api(input=NumpyNdarray(), output=JSON(), route="/predict")
def predict(input_data: np.ndarray) -> dict:
    logger.info("Received prediction request with shape %s", input_data.shape)
    try:
        with Timer(REQUEST_LATENCY):
            result = model_runner.run(input_data)
        PREDICTION_COUNT.inc()
        logger.info("Prediction completed successfully")
        return {"prediction": result.tolist() if hasattr(result, "tolist") else result}
    except Exception as exc:
        ERROR_COUNT.inc()
        logger.error("Prediction failed: %s", exc)
        return {"error": str(exc)}
