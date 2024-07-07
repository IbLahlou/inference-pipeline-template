import {{cookiecutter.model_framework}} as ml_lib

def load_model(model_path):
    model = ml_lib.load(model_path)
    model.eval()
    return model
