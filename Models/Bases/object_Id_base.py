from bson import ObjectId
from pydantic import BaseModel, Field, validator

class Object_Id(ObjectId):
    @classmethod
    def __get_validators_(cls):
        yield cls.validate
    
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError(' Invalide ObjectId')
        return ObjectId(v)
    
    @classmethod
    def __modify__schema__(cls, field_schema):
        field_schema.update(type="string")
        
    print('Object_id ok')