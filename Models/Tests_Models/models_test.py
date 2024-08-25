from bson import ObjectId
from Models.models_model import Models
models = Models(
    model_name='teste',
    version='version 0.0',
    metadata={"version":1, "project_name": "analise"}
)
print("Models test it is ok")
