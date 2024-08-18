from fastapi import FastAPI
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from contextlib import asynccontextmanager as assincrono
from Database import db_conn, db_off, cl
from Collections import user

user
@assincrono
async def lifespan(app: FastAPI):
    async with db_conn():
        print('database connection')
        yield
        db_off()
        print('database closed')
        
app = FastAPI(lifespan=lifespan)
@app.get("/")
async def execute_api():
    return {"detail":"Api Running"}


@app.get("/check_bd")
async def check_bd():
    return{"Connection": db_conn()}
