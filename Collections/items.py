import pymongo
from bson import ObjectId

def items_collection(db_cliente):
    bd = db_cliente
    items_collection = {
        "$jsonSchema":{
            "bsonType":"oject",
            "properties":{
                "_id":f"{ObjectId}",
                "name": {
                    "bsonType":"string",
                    "description": "Name of the Item"
                    },
                "category": {
                    "bsonType": "string",
                    "description": "Name of the Category"
                    },
                "tags": {"key": "value"},
                "createed_at": "datetime",
                "update_at":"datetime"
            }
        }
    }