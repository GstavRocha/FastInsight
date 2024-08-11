import pymongo
from bson import ObjectId
from datetime import datetime


def create_user_collection(db_client):
    db = db_client
    user_collection = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["username", "email", "preferences", "created_at", "updated_at"],
            "properties": {
                "username": {
                    "bsonType": "string",
                    "description": "User Name should an string"
                },
                "email": {
                    "bsonType": "string",
                    "description": "User Email should an string"
                },
                "preferences": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "string"
                    },
                    "description": "preferences for this user",
                },
                "history": {
                    "bsonType": "array",
                    "items": {
                        "required": ["item_id", "timestamp"],
                        "properties": {
                            "item_id": {
                                "bsonType": "objectId",
                                "description": "Item id should be an ObjectId"
                            },
                            "timestamp": {
                                "bsonType": "date",
                                "description": "timestamp should be an date"
                            }
                        }
                    },
                    "created_at": {
                        "bsonType": "date",
                        "description": "Date of creation should be an date"
                    },
                    "updated_at": {
                        "bsonType": "date",
                        "description": "Date of last update should be an date"
                    }

                }

            }
        }
    }
    db.create_collection(user_collection, validation=user_collection)
    print("User collection created successfully")
