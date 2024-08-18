from .utils import check_and_create_collection

item = {
    "_id":"ObjectId",
    "description": "string",
    "category": "string",
    "tag": ["string","required"],
    "metadata": {"key": "value"},
    "created_at": "datetime",
    "updated_at": "datetime"
    
}
check_and_create_collection("ITEM",item)