"""Shared utilities for preprocessing, validation, and data transforms."""

from __future__ import annotations

import numpy as np


def validate_input(data: np.ndarray, expected_dims: int = 2) -> np.ndarray:
    arr = np.asarray(data)
    if arr.ndim < expected_dims:
        arr = np.expand_dims(arr, axis=0)
    return arr
