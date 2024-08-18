from .utils import check_and_create_collection

session = {
    "_id": "ObjectId",
    "user_id":"ObjectId",
    "session_start": "datetime",
    "device_info": "string",
    "location":"string",
    "metadata":{"key": "value"}
}

check_and_create_collection("SESSION", session)