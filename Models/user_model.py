from pydantic import BaseModel,Field,EmailStr
from typing import Optional,List
from Bases.object_Id_base import Object_Id
from Bases.config_base import Config_Base
from Bases.id_base import Base_Id
from Bases.history_item_base import History_Item
from datetime import datetime

class User(BaseModel):
    id: Optional[Object_Id] = Field(default_factory=Object_Id, alias="_id")
    username: str
    email: EmailStr
    preference:  List[str]=[]
    history: List[History_Item()]=[]
    created_at: Optional[datetime]=Field(default_factory=datetime.now().time())
    updated_at: Optional[datetime]=Field(default_factory=datetime.now().time())
    
    class Config(Config_Base):
        pass 
