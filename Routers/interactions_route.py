from pprint import pprint
from fastapi import FastAPI,APIRouter, Query, HTTPException
from pymongo import MongoClient
from Models.user_model import User
from Models.items_model import Items
from Models.interactions_model import Interactions
from Models.generate_id import generate_id
from Database import db_conn
from datetime import datetime
from typing import Dict, Optional, Union, List

interactions_router = APIRouter()
@interactions_router.get("/all_interactions/", tags=["Interactions"])
async def get_interactions():
    database = db_conn()
    collection = database["Interactions"]
    results = list(collection.find())
    for result in results:
        result["id_urse"] = str(result["_id"])
    return {"200":results}

@interactions_router.post("/interactions", tags=["Interactions"])
async def  new_interaction(id_user: str,id_item:str ,interaction: Interactions):
    database = db_conn()
    interactions_collection = database["Interactions"]
    user_collection = database["USER"]
    item_collection = database["Items"]
    user = user_collection.find_one({"id": id_user})
    item = item_collection.find_one({"id_items": id_item})
    # #check a user and a item
    id = generate_id()
    new_inter = {
        "id_interactions": id,
        "user_id": user["id"],
        "item_id": item["id_items"],
        "interaction_tipe":interaction.interactions_tipe,
        "metadata": interaction.metadata
    }
    interactions_collection.insert_one(new_inter)
    return {"result": "ok"}
    # if result.inserted_id:
    #     return {"ok":200}
    # raise HTTPException(status_code=400, detail="user id or item id they are mistakes")