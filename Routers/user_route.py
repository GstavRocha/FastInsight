from fastapi import APIRouter, FastAPI, HTTPException
from Database.connection import get_connection as db_conn
from Database.connection import shutdonw_db as db_off
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from Models.user_model import User 
use_routers = APIRouter()

@use_routers.get('/teste', tags=["User_Router"])
def teste_route():
    return{"ok": "already"}
@use_routers.get("/test", tags=['check'])
async def create_user():
    db=db_conn()
    users = (db["USERS"].find())
    return {"db colection", users}