from pprint import pprint
from fastapi import FastAPI,APIRouter, Query, HTTPException
from pymongo import MongoClient
from Models.user_model import User
from Models.items_model import Items
from Models.recomendations_model import Recomendations
from Models.generate_id import generate_id
from Database import db_conn
from datetime import datetime
from typing import Dict, Optional, Union, List

recomendation_router = APIRouter()
@recomendation_router.post("/recommendation", tags=["Recommendations"])
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

@recomendation_router.get("/recommendations/{user_id}", tags=["Recommendations"])
async def get_all_recommendation(user_id:str):
    database = db_conn()
    collection = database["Recomendations"]
    results = collection.find_one({"user_id": user_id})
    if results:
        results["_id"] = str(results["_id"])
        return{"status": 200, "recommendations": results}
    raise HTTPException(status_code=404, detail="No recommendations found for this user")

@recomendation_router.put("/recommendation/{user_id}", tags=["Recommendations"])
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
@recomendation_router.patch("/recommendation/{id_recommendation}", tags=["Recommendations"])
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
