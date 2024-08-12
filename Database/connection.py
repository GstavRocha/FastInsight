import errno
import pymongo
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import time

uri_local = 'mongodb://localhost:27017'


def get_connection(uri):
    uri = uri_local
    try:
        client = pymongo.MongoClient(uri, connect=True)
        db = client.db_FastInsight
        ping = client.admin.command('ping', 5)
        print(db, 'Connected to MongoDB', ping)
    except Exception as err:
        print(err, 'Erro', errno)
    finally:
        print(time.sleep(60))
        client.close()

