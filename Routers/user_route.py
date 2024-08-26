from fastapi import FastAPI,APIRouter, HTTPException,Request, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder 
from pymongo import MongoClient, ReadPreference as PyM
from pymongo.errors import PyMongoError
from Models.user_model import User 
from Database.connection import db_conn
use_routers = APIRouter()
app = FastAPI()
@use_routers.get('/test', tags=['database check'], status_code=200)
async def dbCheck():
    db = db_conn()
    db.get_collection(name='USER')
    return {'teste': 'ok'}


app.include_router(use_routers)
