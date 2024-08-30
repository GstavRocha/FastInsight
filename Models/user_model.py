import uuid
import random
from pydantic import BaseModel,Field,EmailStr
from typing import Optional,List,Dict
from datetime import datetime
from Models.generate_id import generate_id
  
class User(BaseModel):
    id: Optional[str] = Field(default_factory=generate_id, alias='_id')
    username: str
    email: EmailStr
    preference:  List[str]
    history: Optional[List[str]] = Field(default_factory=list)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    
    class Config:
        arbitrary_types_allowed = True
        # json_encoders = {datetime: lambda v: v.isoformat()}
print('User Model')