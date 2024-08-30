from pprint import pprint
import uuid
from fastapi import FastAPI,APIRouter,Query, Body
from fastapi.encoders import jsonable_encoder 
from fastapi.responses import ORJSONResponse
from pymongo import MongoClient, ReadPreference
from Models.user_model import User, Id 
from Database import db_conn
from datetime import date, datetime
from typing import Dict,Optional,Union,List


use_routers = APIRouter()
app = FastAPI()
@use_routers.get('/test', tags=['collection check'], status_code=200)
async def check_collection():
    collection = db_conn()
    db = collection["USER"]
    return {'teste': db.name}

@use_routers.post('/new_user', tags=['New User'])
async def new_user(user: User):
    database = db_conn()
    collection = database["USER"]
    user_dict = user.model_dump(by_alias=True)
    user_dict['id'] = user_dict.pop('_id')
    collection.insert_one(user_dict)
    return {"detail": "ok"}

@use_routers.get('/getUser', tags=["Get User"])
async def get_user(name: str = Query(...)):
    database = db_conn()
    collection = database["USER"]
    user = collection.find_one({"username": name},{
        "_id": 1,
        "id": 1,
        "username": 1,
        "preference": 1,
        "history": 1,
        "created_at": 1,
        "updated_at": 1    
    })
    print(user)
    return{"ok": 200}

@use_routers.get('/get_id/{user_id}', tags=['Get id User'])
async def get_user_id(user_id:str):
    database = db_conn()
    collection = database['USER']
    user = collection.find_one({"id": user_id},{
        "_id":1,
        "usermane": 1,
        "preference": 1,
        "history": 1
    })
    print(user)
    return{"ok": 200}
@use_routers.get("/get_many", tags=["Get All Users"])
async def get_users():
    db = db_conn()
    collection = db['USER']
    users = list(collection.find())
    pprint(users)
    return {"ok",200}