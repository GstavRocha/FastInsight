from Database import db_conn as db
from options import codec_options
import pymongo as mongo
user = {
    "_id":"ObjectId",
    "username":"string",
    "email":"string",
    "history": [{"item_id": "ObjectId", "timestamp": "datetime"}],
    "created_at": "datetime",
    "updated_at": "datetime"
}

mongo.create_collection(user, codec, check_exists=True)

PÁREIAAQ