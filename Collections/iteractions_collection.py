from .utils import check_and_create_collection

interactions = {
    "_id":"ObjectId",
    "user_id":"ObjectId",
    "item_id":"ObjectId",
    "interaction_type": "string", #ex view, click, purchase
    "timestamp": "datetime",
    "metadata":{"key": "value"}
}

check_and_create_collection("INTERACTIONS", interactions)