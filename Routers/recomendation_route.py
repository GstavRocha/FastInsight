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
@recomendation_router.post("/recomendation", tags=["Recomendations"])
async def get_user_id(recomendation_check: str, recomendation:Recomendations):
    database = db_conn()
    collection = database["Recomendations"]
    user_collection = database["USER"].find_one({"id": recomendation_check})
    id_recomedation = generate_id()
    recomendation_data = {
        "id_recomendation": id_recomedation,
        "create_at": datetime.now()
    }
    if user_collection:
        recomendation_data["user_id"] = user_collection["id"]
        collection.update_one(
            {"user_id": user_collection["id"]},
            {"$set": recomendation_data},
            upsert=True
        )