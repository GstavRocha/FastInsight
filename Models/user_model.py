from pydantic import BaseModel,Field,EmailStr
from typing import Optional,List,Dict
from bson import ObjectId
from datetime import datetime
class User(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='id_user')
    username: str
    email: EmailStr
    preference:  List[str]
    history: List[Dict[ObjectId,datetime]]
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    class Config:
        arbitrary_types_allowed = True
print('User Model')