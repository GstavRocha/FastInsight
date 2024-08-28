from .utils import check_and_create_collection

categories = {
    "_id": int,
    "category_name": "string",
    "parent_category": int, #for subcategories
    "created_at" : "datetime",
    "updated_at": "datetime"
}

check_and_create_collection("CATEGORIES", categories)