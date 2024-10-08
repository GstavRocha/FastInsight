from pprint import pprint
import numpy as np
from fastapi import FastAPI,APIRouter, Query, HTTPException
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient
from Models.user_model import User
from Models.items_model import Items
from Models.recomendations_model import Recomendations
from Models.generate_id import generate_id
from Database import db_conn
from datetime import datetime
from typing import Dict, Optional, Union, List
from Math_utils.cosine_similarity import cosine_similarity

recomendation_routers = APIRouter()
@recomendation_routers.post("/recommendation", tags=["Recommendations"])
async def get_user_id(recomendation_check: str, recomendation:Recomendations):
    database = db_conn()
    collection = database["Recomendations"]
    user_collection = database["USER"].find_one({"id": recomendation_check})
    id_recommedation = generate_id()
    recomendation_data = {
        "id_recomendation": id_recommedation,
        "user_id": user_collection["id"],
        "recomended_items": recomendation.recomended_items,
        "create_at": datetime.now()
    }
    result = collection.update_one(
        {"user_id": user_collection["id"]},
        {"$set": recomendation_data},
        upsert=True
    )
    if result.upserted_id or result.modified_count > 0:
        
        return {"status": "Recommendation created/updated", "id_recommendation": id_recommedation}
    raise HTTPException(status_code=500, detail="Recommendation not created/updated")

@recomendation_routers.get("/recommendations/{user_id}", tags=["Recommendations"])
async def get_all_recommendation(user_id:str):
    database = db_conn()
    collection = database["Recomendations"]
    results = collection.find_one({"user_id": user_id})
    if results:
        results["_id"] = str(results["_id"])
        return{"status": 200, "recommendations": results}
    raise HTTPException(status_code=404, detail="No recommendations found for this user")

@recomendation_routers.put("/recommendation/{user_id}", tags=["Recommendations"])
async def update_user_recommendation(user_id: str, recommendation: Recomendations):
    database = db_conn()
    collection = database["Recomendations"]
    existing_recommendation = collection.find_one({"user_id": user_id})
    if not existing_recommendation:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    result = collection.update_one(
        {"user_id": user_id},
        {"$set": recommendation.model_dump(exclude_unset=True, exclude={"user_id","_id", "id_recomendation"})}
    )
    if result.modified_count >0:
        updated_recommendation = collection.find_one({"user_id": user_id})
        if updated_recommendation:
            updated_recommendation["_id"] = str(updated_recommendation["_id"])
            return {"status": 200, "recommendation": updated_recommendation}
        raise HTTPException(status_code=404,detail="id user not found")
    raise HTTPException(status_code=404, detail=" Recommendation not Not")
@recomendation_routers.patch("/recommendation/{id_recommendation}", tags=["Recommendations"])
async def update_user_recommendation(id_recommendation: str, recommendation: Recomendations):
    database = db_conn()
    collection = database["Recomendations"]

    existing_recommendation = collection.find_one({"id_recomendation": id_recommendation})
    if not existing_recommendation:
        raise HTTPException(status_code=404, detail="Recommendation not found")
    result = collection.update_one(
        {"id_recomendation": collection["id_recomendation"]},
        {"$set": recommendation.model_dump(exclude_unset=True, exclude={"_id","user_id"})}
    )
    if result.modified_count > 0:
        updated_recommendation = collection.find_one({"id_recomendation": id_recommendation})
        if updated_recommendation:
            updated_recommendation["_id"] = str(updated_recommendation["_id"])
            return {"status": 200, "recommendation": updated_recommendation}
    
    raise HTTPException(status_code=400, detail="Recommendation not updated")

@recomendation_routers.delete("/recommendation/{id_recomendation}", tags=["Recommendations"])
async def delete_recommendation(id_recomendation: str):
    database = db_conn()
    collection = database["Recomendations"]
    result = collection.delete_one({"id_recomendation": id_recomendation})
    if result.deleted_count == 1:
        return {"status": "Recommendation deleted"}
    raise HTTPException(status_code=404, detail="No found Recommendation")

@recomendation_routers.get("/recommend/{user_id}", tags=["Recommendations"], description="Recomendation and using coseno similarity")
def recommend_items(user_id: str):
    database = db_conn()
    user_embedding_collection = database["User_Embeddings"]
    item_embedding_collection = database["Item_Embeddings"]
    item_collection = database["Items"]
    insert_recomendations=database["Recomendations"]

    user_embedding = user_embedding_collection.find_one({"user_id": user_id})
    if not user_embedding:
        raise HTTPException(status_code=404, detail="User embedding not found")
    
    user_vector = user_embedding["embedding_vector"]
    recommendations = []
    for item in item_collection.find():
        item_id = item["id_items"]
        item_embedding = item_embedding_collection.find_one({"item_id": item_id})

        if item_embedding:
            item_vector = item_embedding["embedding_vector"]
            similarity = cosine_similarity(user_vector, item_vector)
            recommendation = {
                "item_id": item_id,
                "user_id": user_id,
                "item_name": item["name"],
                "similarity": similarity,
                "timestamp": datetime.now()
            }
            recommendations.append(recommendation)
            json_recommendation = jsonable_encoder(recommendation)
            insert_recomendations.insert_one(json_recommendation)
    recommendations.sort(key=lambda x: x["similarity"], reverse=True)
    
    return {"recommendations": recommendations}
