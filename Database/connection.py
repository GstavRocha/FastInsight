from dotenv import load_dotenv
from pymongo import MongoClient
from dotenv import dotenv_values

load_dotenv()
config = dotenv_values(".env")
def db_conn():
    global client
    try:
        print("Attmeping to connect MongoDb")
        client = MongoClient(config["URI_MONGO"])
        db = client[config["MONGO_NAME"]]
        print('connect to database')
        return db
        
    except Exception as err:
        print('Erro', err)
        return {'Erro':err}
    
def db_off():
    if client:
        client.close()
        print("Db connection Ended")
