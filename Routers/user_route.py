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
@use_routers.get('/test', tags=['database check'], status_code=200)
async def dbCheck():
    collection = db_conn()
    db = collection["USER"]
    return {'teste': db.name}

@use_routers.post('/new_user')
async def new_user(user: User):
    database = db_conn()
    collection = database["USER"]
    user_dict = user.to_dict()
    query = collection.insert_one(user_dict)
    return {"detail": user_dict}


# @use_routers.post('/new_user')
# async def new_user(
#     id: Optional[Id],
#     email: str,
#     username: str,
#     userprefer: List[str],
#     userhist: Optional[Dict[Optional[Id], datetime]] = Body(None)  # Corrigido para receber um dicionário
# ):
#     user_id = id
#     usermail = email
#     user = username
#     user_prefe = userprefer
    
#     # Inicializa userhist se for None
#     if userhist is None:
#         userhist = {}

#     # Adiciona um novo histórico
#     id_history = Id # Converte o ID para string para usar como chave
#     date_history = datetime.now()
#     userhist[id_history] = date_history

#     return {"detail": userhist}