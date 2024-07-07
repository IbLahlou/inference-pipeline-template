from bentoml import BentoService, api, env
from bentoml.io import Ndarray

class {{cookiecutter.model_service_name}}(BentoService):

    @env(infer_pip_packages=True)
    {% if cookiecutter.batchable == "yes" %}
    @api(input=Ndarray(dtype="float32", shape=({{cookiecutter.batch_dim}}, 224, 224, 3)), output=Ndarray(dtype="float32"), batch=True)
    def predict(self, input_batch):
        # Prediction logic for batch inputs
        return self.artifacts.model(input_batch)
    {% else %}
    @api(input=Ndarray(dtype="float32", shape=(224, 224, 3)), output=Ndarray(dtype="float32"))
    def predict(self, input):
        # Prediction logic for single input
        return self.artifacts.model(input)
    {% endif %}
