import errno
import time
from pymongo import MongoClient

uri_local = 'mongodb://localhost:27017'



def get_connection(app,uri):
    uri = uri_local
    try:
        app.mongodb_client= MongoClient([f"{uri}"]);
        return('connect to database')
        
    except Exception as err:
        print(err, 'Erro', errno)
    finally:
        print(time.sleep(6))
    
def shutdonw_db(app):
    app.mongodb_client.close()
    print("data base is closed")
