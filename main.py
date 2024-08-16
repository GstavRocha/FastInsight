from fastapi import FastAPI
from contextlib import asynccontextmanager
from Database import db_link, db_conn, db_off
app = FastAPI()
db = db_link

@app.get("/")
async def execute_api():
    return {"detail":"Api Running"}

@asynccontextmanager
async def connect_db():
    conn = await db_conn(app, db)
    off = await db_off()
    try:
        yield conn
    finally:
        await off

