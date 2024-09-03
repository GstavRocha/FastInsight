
from pprint import pprint
from fastapi import FastAPI,APIRouter, Query, HTTPException
from pymongo import MongoClient
from Models.user_model import User
from Models.items_model import Items
from Models.embeddings_model import Embeddings
from Models.items_embeddings_model import Item_Embeddings
from Models.generate_id import generate_id
from Database import db_conn
from datetime import datetime
from typing import Dict, Optional, Union, List

items_embeddings_routers = APIRouter()
@items_embeddings_routers.post("/item_embeddings", tags=["Item Embeddings"])
async def add_item_embedding(item_id: str, embedding_vector: List[float]):
    database = db_conn()
    collection = database["Item_Embeddings"]
    items_collection = database["Items"].find_one({"id_items":item_id})
    items_name = items_collection["name"]
    if not items_collection:
        raise HTTPException(status_code=404, detail="id_items not found")
    embedding_data = {
        "item_id": item_id,
        "item_name": items_name,
        "embedding_vector": embedding_vector,
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    result = collection.insert_one(embedding_data)
    return {"status": 200, "id_embedding": str(result.inserted_id)}

@items_embeddings_routers.get("/item_embeddings/{item_id}", tags=["Item Embeddings"])
async def get_item_embedding(item_id: str):
    database = db_conn()
    collection = database["Item_Embeddings"]
    item_embedding = collection.find_one({"item_id": item_id})
    if not item_embedding:
        raise HTTPException(status_code=404, detail="Item embedding not found")
    return item_embedding
@items_embeddings_routers.patch("/item_embeddings/{item_id}/add_vector", tags=["Item Embeddings"])
async def add_vector_item_embedding(item_id: str, add_vector: List[float]):
    database = db_conn()
    collection = database["Item_Embeddings"]
    item_embedding = collection.find_one({"item_id": item_id})
    if not item_embedding:
        raise HTTPException(status_code=404, detail="Item embedding not found")
    result = collection.update_one(
        {"item_id": item_id},
        {"$push": {"embedding_vector": {"$each": add_vector}}}
    )
    if result.modified_count > 0:
        updated_embedding = collection.find_one({"item_id": item_id})
        return {"status": 200, "embedding_vector": updated_embedding["embedding_vector"]}
    
    raise HTTPException(status_code=400, detail="Item embedding not updated")
@items_embeddings_routers.delete("/items_embeddings/{item_id}", tags=["Item Embeddings"])
async def delete_item_embedding(item_id: str):
    database = db_conn()
    collection = database["Item_Embeddings"]
    result = collection.delete_many({"item_id": item_id})
    if result.deleted_count > 0:
        return {"status": 200, "Item_embeddings": "was deleted"}
    raise HTTPException(status_code=404, detail="item id not found")

