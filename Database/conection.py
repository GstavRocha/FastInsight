from pymongo import MongoClient

uri_local = 'mongodb://localhost:27017'
client = MongoClient(uri_local)
try:
    client = client.server_info()
except Exception as err:
    raise Exception(err,"NOT CONNECTED")
finally:
    client.close()
    if client.close() is True:
        print("Connection Closed")
    else:
        print("Connection Not Closed")

