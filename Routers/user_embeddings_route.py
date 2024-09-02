
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

user_embedding_router = APIRouter()
@user_embedding_router.post("/user_embeddings/{user_id}", tags=["User Embeddings"])
async def add_user_embedding(user_id: str, embedding_vector: List[float]):
    database = db_conn()
    collection = database["User_Embeddings"]
    embedding_data= {
        "user_id": user_id,
        "embedding_vector": embedding_vector,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    result = collection.update_one(
        {"user_id": user_id},
        {"$set": embedding_data},
        upsert=True
    )
    if result.matched_count > 0 or result.upserted_id:
        return {"status": "Embedding add or update"}
    raise HTTPException(status_code=500, detail="Failed to add/update embedding")
@user_embedding_router.patch("/user_embeddings/{user_id}/{add_vector}", tags=['User Embeddings'])
async def add_vector_user_embeddings(user_id_check: str, add_vector: float):
    database = db_conn()
    collection = database["User_Embeddings"]
    user_collection = database["Embeddings"].find_one({"id": user_id_check}) 
    
    if user_collection:
        collection = database["User_Embeddings"]
        result = collection.update_one(
            {"user_id": user_id_check},
            {"$push": {"embedding_vector": add_vector}},
            upsert=True 
        )
        
        if result.modified_count >= 0:
            updated_embedding = collection.find_one({"user_id": user_id_check})
            return {"status": 200, "embedding_vector": updated_embedding["embedding_vector"]}
        
        raise HTTPException(status_code=400, detail="Collection not updated")
    
    raise HTTPException(status_code=404, detail="User ID not found")

    
        
@user_embedding_router.get("/user_embeddings/{user_id}", tags=['User Embeddings'])
async def get_user_embedding(user_id: str):
    database = db_conn()
    collection = database["User_Embeddings"]
    user_embedding = collection.find_one({"user_id": user_id})
    if user_embedding:
        return {"user_id": user_embedding["user_id"], "embedding_vector": user_embedding["embedding_vector"]}
    raise HTTPException(status_code=404, detail="Embedding not found")
