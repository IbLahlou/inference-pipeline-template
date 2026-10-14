"""Save a placeholder model to the BentoML model store.

Replace this with your actual model loading / training logic.
The script must produce a model artifact that the service file can load.
"""

import bentoml
import numpy as np

{% if cookiecutter.model_framework == "pytorch" -%}
import torch
import torch.nn as nn


class SimpleModel(nn.Module):
    def __init__(self, input_dim=4, output_dim=3):
        super().__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.linear(x)


model = SimpleModel()
model.eval()

tag = bentoml.pytorch.save_model(
    "{{ cookiecutter.model_name }}",
    model,
)
{% elif cookiecutter.model_framework == "tensorflow" -%}
import tensorflow as tf


model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation="relu", input_shape=(4,)),
    tf.keras.layers.Dense(3, activation="softmax"),
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy")

tag = bentoml.tensorflow.save_model(
    "{{ cookiecutter.model_name }}",
    model,
)
{% endif -%}

print(f"Model saved: {tag}")
