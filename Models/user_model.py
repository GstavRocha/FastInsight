import uuid
import random
from pydantic import BaseModel,Field,EmailStr
from typing import Optional,List,Dict
from datetime import datetime

def generate_item_id()->int:
    return random.randint(1,100000000000)
def generate_id() -> str:
    return str(uuid.uuid4())
    
class Id(BaseModel):
    id: Optional[str]= Field(default_factory=generate_id)
class Item_Id(BaseModel):
    item_it: Optional[int] = Field(default_factory=generate_item_id)

class User(BaseModel):
    id: Optional[str] = Field(default_factory=generate_id, alias='id')
    username: str
    email: EmailStr
    preference:  List[str]
    history: Optional[List[str]] = Field(default_factory=list)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {datetime: lambda v: v.isoformat()}
print('User Model')