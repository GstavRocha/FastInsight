import uuid
import random
from bson import ObjectId
from pydantic import BaseModel,Field,EmailStr
from typing import Optional,List,Dict
from datetime import datetime
def generate_id() -> str:
    return str(uuid.uuid4())
def generate_item_id()->int:
    return random.randint(1,100000000000)
    
class Id(BaseModel):
    id: Optional[str]= Field(default_factory=generate_id)
class Item_Id(BaseModel):
    item_it: Optional[int] = Field(default_factory=generate_item_id)

class User(BaseModel):
    id: Optional[Id] = Field(default_factory=lambda: Id(id=generate_id()), alias='id_user')
    username: str
    email: EmailStr
    preference:  List[str]
    history: Optional[List[str]] = Field(default_factory=list)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    def to_dict(self):
        data = self.model_dump()
        if 'id' in data and isinstance(data["id"], ObjectId):
            data['id'] = str(data['id'])
        return data 
    
    class Config:
        arbitrary_types_allowed = True
print('User Model')