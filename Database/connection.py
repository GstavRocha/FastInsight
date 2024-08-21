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
        client = MongoClient(config["URI_MONGO"])
        print('connect to database')
        return client[config["MONGO_NAME"]]
        
    except Exception as err:
        print('Erro', err)
        return {'Erro':err}
    
def shutdonw_db():
    client[config["MONGO_NAME"]].close()
    print("Db connection Ended")
