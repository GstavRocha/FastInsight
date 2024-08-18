from .utils import check_and_create_collection

recommendation = {
    "_id": "ObjectId",
    "user_id": "ObjectId",
    "recommended_items": [{"item_id": "ObjectId", "score":"float"}],
    "created_at": "datetime"
}
check_and_create_collection("RECOMMENDATION", recommendation)