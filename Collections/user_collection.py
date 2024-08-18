from Database import db_conn as db
from .utils import check_and_create_collection

user ={
    "_id":"ObjectId",
    "username":"string",
    "email":"string",
    "history": [{"item_id": "ObjectId", "timestamp": "datetime"}],
    "created_at": "datetime",
    "updated_at": "datetime"
}

check_and_create_collection("USER", user)

