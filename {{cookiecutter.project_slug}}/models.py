import torch
import bentoml


# Load the model
model = Model('params')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device).eval()  # Move model to GPU if available

tag = bentoml.pytorch.save_model(
                            "{{cookiecutter.model_name}}",  # model name in the local model store
                            model,      # model instance being saved
                            # signatures={   # model signatures for runner inference
                            # "__call__": {
                            #     "batchable": True,
                            #     "batch_dim": (0,0),
                            #     }
                            # }
                    )

print(f"Model Saved Successfully: {tag}")