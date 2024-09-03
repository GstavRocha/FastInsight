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

interactions_routers = APIRouter()
@interactions_routers.get("/all_interactions/", tags=["Interactions"])
async def get_interactions():
    database = db_conn()
    collection = database["Interactions"]
    results = list(collection.find())
    for result in results:
        result["_id"] = str(result["_id"])
    return {"200":results}

@interactions_routers.post("/interactions", tags=["Interactions"])
async def  new_interaction(id_user: str,id_item:str ,interaction: Interactions):
    database = db_conn()
    interactions_collection = database["Interactions"]
    user_collection = database["USER"]
    item_collection = database["Items"]
    user = user_collection.find_one({"id": id_user})
    item = item_collection.find_one({"id_items": id_item})
    id = generate_id()
    new_inter = {
        "id_interactions": id,
        "user_id": user["id"],
        "item_id": item["id_items"],
        "interaction_tipe":interaction.interactions_tipe,
        "metadata": interaction.metadata
    }
    if user["id"] is not False and item['id_items'] is not False:
        interactions_collection.insert_one(new_inter)
        return {"result": "ok"}
    raise HTTPException(status_code=400, detail="Some Error on Request")

@interactions_routers.get("/interactions/user/", tags=["Interactions"])
async def get_id_interactions(user_id: str = Query(...)):
    database = db_conn()
    collections = database["Interactions"]
    user_interactions_cursor = collections.find({"user_id": user_id})
    user_interactions = []
    for interaction in user_interactions_cursor:
        interaction["_id"] = str(interaction["_id"])
        user_interactions.append(interaction)
    if user_interactions:
        pprint(user_interactions)
        return {"ok": 200, "interactions": user_interactions}
    raise HTTPException(status_code=404, detail="User not found", headers="ErroR")

@interactions_routers.get("/interactions/item/", tags=["Interactions"])
async def get_id_interactions(item_id: str = Query(...)):
    database = db_conn()
    collections = database["Interactions"]
    item_interactions_cursor = collections.find({"item_id": item_id})
    item_interactions = []
    for interaction in item_interactions_cursor:
        interaction["_id"] = str(interaction["_id"])
        item_interactions.append(interaction)
    if item_interactions:
        pprint(item_interactions)
        return {"ok": 200, "interactions": item_interactions}
    raise HTTPException(status_code=404, detail="Item not found", headers="ErroR")

@interactions_routers.put("/interaction/{interaction_id}", tags=["Interactions"])
async def get_id_interaction(interatcion_id: str, interactions: Interactions):
    database = db_conn()
    collection = database["Interactions"]
    update_data = interactions.model_dump(exclude_unset=True, exclude={"_id", "id_interactions", "user_id", "item_id"})
    result = collection.update_one({"id_interactions": interatcion_id},{"$set": update_data})
    if result.matched_count == 1:
        return{"detail": 200,
               "user_id": interactions.user_id,
               "item_id": interactions.item_id,
               "metadata": interactions.metadata
        }
    HTTPException(status_code=400, detail="not found")

@interactions_routers.delete("/interactions/{interaction_id}", tags=["Interactions"])
async def delete_interaction(interaction_id):
    database = db_conn()
    collection = database["Interactions"]
    result = collection.delete_one({"id_interactions": interaction_id})
    if result.deleted_count == 1:
        return {"detail": 200}
    raise HTTPException(status_code=400, detail=" It've some Problem")