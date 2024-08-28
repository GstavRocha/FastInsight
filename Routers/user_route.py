from fastapi import FastAPI,APIRouter
from fastapi.encoders import jsonable_encoder 
from pymongo import MongoClient, ReadPreference
from Models.user_model import User 
from Database import db_conn
use_routers = APIRouter()
app = FastAPI()
@use_routers.get('/test', tags=['database check'], status_code=200)
async def dbCheck():
    check = db_conn["USER"]
    return {'teste': check.name}
