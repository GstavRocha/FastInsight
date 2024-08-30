from pprint import pprint
from fastapi import FastAPI,APIRouter,Query, Body, HTTPException
from fastapi.encoders import jsonable_encoder 
from fastapi.responses import ORJSONResponse
from pymongo import MongoClient, ReadPreference
from Models.user_model import User
from Models.generate_id import generate_id
from Database import db_conn
from datetime import date, datetime
from typing import Dict,Optional,Union,List
from datetime import datetime


use_routers = APIRouter()
app = FastAPI()
@use_routers.get('/test', tags=['DATABASE CHECK'], status_code=200)
async def check_collection():
    collection = db_conn()
    db = collection["USER"]
    return {'teste': db.name}

@use_routers.post('/new_user/', tags=['USER ROUTES'], description='This endpoint allows you to create a new user. For to create you will need a json')
async def new_user( user: User):
    database = db_conn()
    collection = database["USER"]
    user_dict = user.model_dump(by_alias=True,exclude="_id")
    id = generate_id()
    created_at= datetime.now()
    updated_at= datetime.now()
    collection.insert_one(
        {
            "id": id,
            "username": user.username,
            "email": user.email,
            "preference": user.preference,
            "history": user.history,
            "created_at": created_at,
            "updated_at": updated_at
        },{"$set": user_dict}
    )
    return {"detail": "ok"} #to do verication about exiting user

@use_routers.get('/getUser', tags=['USER ROUTES'], description=' seacher ato get user Id return the firsts values')
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
    if user:
        user["_id"] = str(user['_id'])
        return{"ok": user}

@use_routers.get('/get_id/{user_id}', tags=['USER ROUTES'], description='return ')
async def get_user_id(user_id:str):
    database = db_conn()
    collection = database['USER']
    user = collection.find_one({"id": user_id},{
        "_id":1,
        "username": 1,
        "preference": 1,
        "history": 1
    })
    if user:
        user["_id"] = str(user["_id"])
        return{"ok": user}
    # To write about errors
@use_routers.get("/get_many", tags=['USER ROUTES'])
async def get_all_users():
    db = db_conn()
    collection = db['USER']
    users = list(collection.find())
    result = jsonable_encoder(users)
    return {"ok":result}

@use_routers.put('/user/{user_id}', tags=['USER ROUTES'])
async def update_user(user_id: str, user: User):
    database = db_conn()
    collection = database['USER']
    update_data = user.model_dump(exclude_unset=True, exclude={"_id","id"})
    result = collection.update_one({"id": user_id}, {"$set": update_data})
    if result.matched_count == 1:
        return {"detail": "User updated","user": update_user}
    else:
        return {"detail": "User not found"}, 404
@use_routers.delete('/user/{user_id}', tags=['USER ROUTES'])
async def delete_user(user_id: str):
    database = db_conn()
    collection = database['USER']
    result = collection.delete_one({"id": user_id})
    if result.deleted_count == 1:
        return {"detail": 200}
    return {"detail": "not found"},404
@use_routers.patch("/user/{user_id}/{add_history}", tags=['USER ROUTES'])
async def add_history(user_id: str, add_history: str):
    database = db_conn()
    collection = database['USER']
    result = collection.update_one(
        {"id": user_id},
        {"$push": {"history": add_history}}
    )
    if result.modified_count == 1:
        return {"detail": 200}
    raise HTTPException(status_code=404, detail=" Not found")
@use_routers.patch("/users/{user_id}/{add_preference}", tags=['USER ROUTES'])
async def add_preference(user_id: str, add_preference: str):
    database = db_conn()
    collection = database['USER']
    result = collection.update_one(
        {"id": user_id},
        {"$push": {"preference": add_preference}}
    )
    if result.modified_count == 1:
        return {"detail": 200}
    raise HTTPException(status_code=200, detail="Not found")
    
