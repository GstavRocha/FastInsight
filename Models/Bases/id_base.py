from pydantic import BaseModel,Field
from typing import Optional, List
from bson import ObjectId
# from object_Id_base import Object_Id

class Base_Id(BaseModel):
    id: Optional[ObjectId]= Field(default_factory=ObjectId, alias="id")

    class Config:
        arbitrary_types_allowed=True
        print('id bases Ok')
        pass