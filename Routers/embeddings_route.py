from pprint import pprint
from fastapi import FastAPI,APIRouter, Query, HTTPException
from pymongo import MongoClient
from Models.user_model import User
from Models.items_model import Items
from Models.embeddings_model import Embeddings
from Models.generate_id import generate_id
from Database import db_conn
from datetime import datetime
from typing import Dict, Optional, Union, List

embeddings_router = APIRouter()
@embeddings_router.post("/embeggings", tags=['Embeddings'])
async def new_embedding(embedding_check: str, embeddings: Embeddings):
    database = db_conn()
    collection = database["Embedding"]
    user_collection = database["USER"].find_one({"id": embedding_check})
    item_collection = database["Items"].find_one({"id_items": embedding_check})
    id_embeddings = generate_id()
    embedding_data = {
        "id_embeddings": id_embeddings,
        "embedings_vector":embeddings.embedings_vector,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    if user_collection:
        embedding_data["entity_id"] = user_collection["id"]
        embedding_data["entity_type"] = user_collection["username"]
        collection.update_one(
            {"entity_id": user_collection["id"]}, 
            {"$set": embedding_data},             
            upsert=True                           
        )
        return {"Embedding": "USER",
            "id_embeddings": embedding_data["id_embeddings"],
            "entity_type": embedding_data["entity_type"],
            "embedings_vector": embedding_data["embedings_vector"],
            "created_at": embedding_data["created_at"],
            "updated_at": embedding_data["updated_at"]
                }
    elif item_collection:
        embedding_data["entity_id"] = item_collection["id_items"]
        embedding_data["entity_type"] = item_collection["name"]
        collection.update_one(
            {"entity_id": item_collection["id_items"]},
            {"$set": embedding_data},                    
            upsert=True                                  
        )
        return {"Embedding": "Items",
            "id_embeddings": embedding_data["id_embeddings"],
            "entity_type": embedding_data["entity_type"],
            "embedings_vector": embedding_data["embedings_vector"],
            "created_at": embedding_data["created_at"],
            "updated_at": embedding_data["updated_at"]
                }
    else:
        raise HTTPException(status_code=400, detail="ID not found in user or item collections")

@embeddings_router.patch("/embeddings/{add_vector}/{id_embedding}", tags=['Embeddings'])
async def add_vector(add_vector: float, id_embedding: str):
    database = db_conn()
    collection = database["Embedding"]
    embedding_check = collection.find_one({"id_embeddings":id_embedding})
    if not embedding_check:
        raise HTTPException(status_code=404, detail="Embedding Not Found")
    result = collection.update_one(
        {"id_embeddings": id_embedding},
        {"$push": {"embedings_vector": add_vector}}
    )

    if result.modified_count == 1:
        updated_collection= collection.find_one({"id_embeddings": id_embedding})
        return {"embedding vector": "was modified",
                "embedding_vector": updated_collection["embedings_vector"]
                }
    else:
        raise HTTPException(status_code=404, detail="Embedding not found")

@embeddings_router.get("/embeddings", tags=["Embeddings"])
async def all_embeddings():
    database = db_conn()
    collection = database["Embedding"]
    embeddings = list(collection.find())
    for embedding in embeddings:
       embedding["_id"] = str(embedding["_id"])
    return {"embeddings": embeddings}

@embeddings_router.get("/embeddings/{entity_id}", tags=["Embeddings"])
async def get_entity_id(entity_id:str):
    database = db_conn()
    collection = database["Embedding"]
    results = collection.find({"entity_id": entity_id})
    embeddgins = []
    for result in results:
        result["_id"] = str(result["_id"])
        embeddgins.append(result)
    return {"result":embeddgins}
@embeddings_router.delete("/embeddings/{id_embedding}", tags=["Embeddings"])
async def delete_embedding(id_embedding: str):
    database = db_conn()
    collection = database["Embedding"]
    result = collection.delete_one({"id_embeddings": id_embedding})
    if result.deleted_count == 1:
        return {"was deleted id_embedding", 200}
    raise HTTPException(status_code=404, detail=" id_embedding not found")
 