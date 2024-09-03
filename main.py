from fastapi import FastAPI
from pymongo import MongoClient
# from Routers.sessions_route import session_routers
from Routers import use_routers,items_routers, interactions_routers, embeddings_routers, user_embedding_routers, recomendation_routers, items_embeddings_routers
from pymongo.errors import ConnectionFailure
from contextlib import asynccontextmanager
from Database import db_conn, db_off
from Collections import *
from Models import *
@asynccontextmanager
async def lifespan(app: FastAPI):
    db_conn()
    print('database connection')
    yield
    db_off()
    print('database closed')
        
try:
    app = FastAPI(lifespan=lifespan)
    @app.get("/", tags=["Main"])
    async def execute_api():
        return {"detail":"Api Running"}
   
    @app.get("/check_bd", tags=["Main"])
    async def check_bd():
        db = db_conn()
        return{"Connection":db.name}
    
    db_off()
except Exception as err:
    print("erro MAIN -->", err)
    
app.include_router(use_routers)
app.include_router(items_routers)
app.include_router(interactions_routers)
app.include_router(embeddings_routers)
app.include_router(recomendation_routers)
app.include_router(user_embedding_routers)
app.include_router(items_embeddings_routers)