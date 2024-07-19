import os
import bentoml
import torch
import time



matcher = bentoml.pytorch.load_model("{{cookiecutter.model_name}}:latest")
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

tag = bentoml.pytorch.save_model(
                            "{{cookiecutter.model_name}}",  # model name in the local model store
                            matcher,      # model instance being saved
                            # signatures={   # model signatures for runner inference
                            # "__call__": {
                            #     "batchable": True,
                            #     "batch_dim": (0,0),
                            #     }
                            # }
                    )

print(f"Model Saved Successfully: {tag}")

def inference_pipeline():
    pass

model = inference_pipeline()

start_time = time.time() 
result = model()
end_time = time.time() 
similarity_time = end_time - start_time

print(similarity_time)
print(result)
