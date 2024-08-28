from .utils import check_and_create_collection

item = {
    "_id":int,
    "description": "string",
    "category": "string",
    "tag": ["string","string"],
    "metadata": {"key": "value"},
    "created_at": "datetime",
    "updated_at": "datetime"
    
}
check_and_create_collection("ITEM",item)