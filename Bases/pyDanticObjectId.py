import pdb
from pydantic import BaseModel
from bson.objectid import ObjectId as Bson_ObjectId

pdb.set_trace()
class PyDantic_ObjectId_Base(Bson_ObjectId):
    @classmethod
    def __get__validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls,v):
        if not isinstance(v,Bson_ObjectId):
            raise TypeError('ObjectId Required')
        return str(v)
print('Ok')