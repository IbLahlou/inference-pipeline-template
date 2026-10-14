import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from utils import validate_input


def test_validate_input_1d():
    arr = validate_input(np.array([1, 2, 3]))
    assert arr.ndim == 2
    assert arr.shape == (1, 3)


def test_validate_input_2d():
    arr = validate_input(np.array([[1, 2], [3, 4]]))
    assert arr.ndim == 2
    assert arr.shape == (2, 2)
