from fastapi import FastAPI
from pymongo import MongoClient
from Routers.user_route import use_routers
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
    @app.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html_cdn():
        return get_swagger_ui_html(
            openapi_url=app.openapi_url,
            title=f"{app.title} - Swagger UI",
            swagger_css_url="https://cdn.jsdelivr.net/gh/Itz-fork/Fastapi-Swagger-UI-Dark/assets/swagger_ui_dark.min.css"
)
    @app.get("/check_bd", tags=["Main"])
    async def check_bd():
        db = db_conn()
        return{"Connection":db.name}
    
    db_off()
except Exception as err:
    print("erro MAIN -->", err)
    
app.include_router(use_routers)