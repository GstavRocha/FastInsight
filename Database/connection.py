import errno
import time
from dotenv import load_dotenv
from pymongo import MongoClient
from dotenv import dotenv_values
client = None

load_dotenv()
config = dotenv_values(".env")
def get_connection():
    global client
    try:
        client = MongoClient(config["URI"])
        client.admin.command({"ping":1})
        print('connect to database')
        return client[config["MONGO_NAME"]]
        
    except Exception as err:
        print(err, 'Erro', errno)
        return {'lost':'connection'}
    
def shutdonw_db():
    client[config["MONGO_NAME"]].close()
    print("Db connection Ended")
