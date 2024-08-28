from pydantic import BaseModel,Field,EmailStr
from typing import Optional,List,Dict
from datetime import datetime
class User(BaseModel):
    id: Optional[int] = Field(default_factory=int,required=False ,alias='id_user')
    username: str
    email: EmailStr
    preference:  List[str]
    history: List[Dict[int,datetime]]
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    class Config:
        arbitrary_types_allowed = True
print('User Model')