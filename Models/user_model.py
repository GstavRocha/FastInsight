from pydantic import BaseModel,Field,EmailStr
from typing import Optional, List
from Bases.object_Id_base import Object_Id
from Bases.config_base import Base_Config
from Bases.id_base import Base_Id
from datetime import datetime

class User(BaseModel):
    id: Optional[Object_Id] = Field(default_factory=Object_Id, alias="_id")
    username: str
    email: EmailStr
    preference:  List[str]=[]
    history: List[Object_Id]=[]
    created_at: Optional[datetime]=Field(default_factory=datetime.UTC)
    updated_at: Optional[datetime]=Field(default_factory=datetime.UTC)
    
    class Base_Config(Base_Id):
        pass 
