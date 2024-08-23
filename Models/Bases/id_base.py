from pydantic import BaseModel,Field
from typing import Optional, List
from Bases.object_Id_base import Object_Id
from Bases.config_base import Base_Config

class Base_Id(BaseModel):
    id: Optional[Object_Id]= Field(default_factory=Object_Id, alias=id)

    class Config(Base_Config):
        pass