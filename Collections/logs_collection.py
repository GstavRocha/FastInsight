from .utils import check_and_create_collection

logs = {
    "_id":int,
    "event_type": "string",
    "description": "string",
    "user_id": int,
    "item_id": int,
    "timestamp":"datetime",
    "metadata": {"key": "value"}
}

check_and_create_collection("LOGS", logs)