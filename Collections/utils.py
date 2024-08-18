from Database import db_conn
from .options import codec_options

def check_and_create_collection(collection_name, colletion):
    database = db_conn()
    new_collection = database[collection_name]
    if collection_name in database.list_collection_names():
        print('Already be')
    else:
        database.create_collection(collection_name)
        new_collection.insert_one(colletion)
        print('The Collection was create')