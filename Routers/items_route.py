from pprint import pprint
import uuid
from fastapi import FastAPI,APIRouter,Query, Body, HTTPException 
from fastapi.encoders import jsonable_encoder 
from fastapi.responses import ORJSONResponse
from pymongo import MongoClient, ReadPreference
from Models.items_model import Items
from Models.generate_id import generate_id
from Database import db_conn,db_off
from datetime import date, datetime
from typing import Dict,Optional,Union,List

items_routers = APIRouter()

@items_routers.get("/get_all_items", tags=["Items"])
async def get_all_itens():
    database = db_conn()
    collection = database['Items']
    items  = list(collection.find())
    for item in items:
        item["_id"] =str(item["_id"])
    return {"items":items}
@items_routers.get("/items/{seach_items}",tags=["Items"])
async def search_items(seach_items: str):
    database =db_conn()
    collection = database["Items"]
    items = list(collection.find({"name": seach_items}))
    for item in items:
        item["_id"] = str(item["_id"])
    return {"itens": items}
@items_routers.get("/item/{search}", tags=["Items"])
async def search_item(search: str):
    database = db_conn()
    collection = database["Items"]
    item = collection.find_one({"name": search}, {
        "id_items":1,
        "name":1,
        "description":1,
        "tags":1,
        "metadata":1
    })
    if item:
        item["_id"] = str(item["_id"])
        return {"ok": item}
    raise HTTPException(status_code=400, detail="Name not found")
  
@items_routers.post("/items/new_item", tags=["Items"])
async def new_items(items: Items):
    database = db_conn()
    collection = database['Items']
    items.model_dump(by_alias=True, exclude="_id")
    if collection.find_one({"$or": [{"name": items.name}, {"description": items.description}]}):
        raise HTTPException(status_code=400, detail="some item already exists.")
    item_id = generate_id()
    created_at= datetime.now()
    updated_at= datetime.now()
    new_item = {
        "id_items": item_id,
        "name": items.name,
        "descrition": items.description,
        "category": items.category,
        "metadata": items.metadata,
        "tags": items.tags,
        "created_at": created_at,
        "updated_at": updated_at
    } 
    insert= collection.insert_one(new_item)
    status = HTTPException(status_code=201, headers="items")
    return {"item": item_id,"status":status }
@items_routers.put("/items/{id_item}" , tags=["Items"])
async def item_update(id_item:str, items: Items):
    database = db_conn()
    collection = database["Items"]
    update_data = items.model_dump(exclude_unset=True, exclude={"_id", "id_items"})
    result = collection.update_one({"id_items": id_item},{"$set": update_data})
    if result.matched_count == 1:
        return {"detail": "Item Updated",
                "name": items.name,
                "description": items.description,
                "category": items.category,
                "tags": items.tags,
                "metadata": items.metadata
                }
    raise HTTPException(status_code=400, detail= "Invalid Data")
@items_routers.delete("/item/{id_item}", tags=["Items"])
async def delete_item(id_item:str):
    database = db_conn()
    collection = database["Items"]
    result = collection.delete_one({"id_items":id_item})
    if result.deleted_count ==1:
        return{"result": 200}
    raise HTTPException(status_code=404, detail="id not found")
    