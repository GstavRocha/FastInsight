import errno
import time
from dotenv import load_dotenv
from pymongo import MongoClient
from dotenv import dotenv_values

load_dotenv()
config = dotenv_values(".env")
print(config["MONGO_NAME"])


# def get_connection(app,uri):
#     try:
#         app.mongodb_client= MongoClient(config["MONGO_NAME"])
#         app.database = app.mongodb_client[["db_FastInsight"]]
#         print('connect to database')
        
#     except Exception as err:
#         print(err, 'Erro', errno)
    
# def shutdonw_db(app):
#     app.mongodb_client.close()
#     print("data base is closed")
