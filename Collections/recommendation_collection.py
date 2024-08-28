from .utils import check_and_create_collection

recommendation = {
    "_id": int,
    "user_id": int,
    "recommended_items": [{"item_id":int, "score":float}],
    "created_at": "datetime"
}
check_and_create_collection("RECOMMENDATION", recommendation)