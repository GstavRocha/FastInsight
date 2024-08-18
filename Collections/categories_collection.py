from .utils import check_and_create_collection

categories = {
    "_id": "ObjectId",
    "category_name": "string",
    "parent_category": "ObjectId", #for subcategories
    "created_at" : "datetime",
    "updated_at": "datetime"
}

check_and_create_collection("CATEGORIES", categories)