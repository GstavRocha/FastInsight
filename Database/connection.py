import errno
import time
from dotenv import load_dotenv
from pymongo import MongoClient
from dotenv import dotenv_values
from fastapi import FastAPI

client = None

load_dotenv()
config = dotenv_values(".env")
def get_connection():
    try:
        global client
        client = MongoClient(config["URI"])
        client_db = client[config["MONGO_NAME"]]
        client.admin.command({"ping":1})
        print(client_db)
        print('connect to database')
        return True
        
    except Exception as err:
        print(err, 'Erro', errno)
        return False
    
def shutdonw_db():
    if client is True:
        client.close()
        print("Db connection Ended")
