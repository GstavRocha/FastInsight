from .utils import check_and_create_collection

models = {
    "_id": int,
    "model_name": "string",
    "version":"string",
    "trained_at": "datetime",
    "metadata": {"key": "value"}
}
check_and_create_collection("MODELS", models)