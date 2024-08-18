from .utils import check_and_create_collection

logs = {
    "_id":"ObjectId",
    "event_type": "string",
    "description": "string",
    "user_id": "ObjectId",
    "item_id": "OjectId",
    "timestamp":"datetime",
    "metadata": {"key": "value"}
}

check_and_create_collection("LOGS", logs)