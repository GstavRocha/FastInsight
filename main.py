from fastapi import FastAPI
from contextlib import asynccontextmanager
from Database import db_link, db_conn, db_off
app = FastAPI()

@app.get("/")
async def execute_api():
    return {"detail":"Api Running"}

@asynccontextmanager
async def db_conn(app, db_link):
    return {"ok": 200}
    
