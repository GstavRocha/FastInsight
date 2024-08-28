from .utils import check_and_create_collection

interactions = {
    "_id":int,
    "user_id":int,
    "item_id":int,
    "interaction_type": "string", #ex view, click, purchase
    "timestamp": "datetime",
    "metadata":{"key": "value"}
}

check_and_create_collection("INTERACTIONS", interactions)