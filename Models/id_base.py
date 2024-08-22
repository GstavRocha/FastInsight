from pydantic import BaseModel,Field
from typing import Optional, List
from PyObject import PyObjectId
from config import Base_Config

class Base_Model_Id(BaseModel):
    id: Optional[PyObjectId]= Field(default_factory=PyObjectId, alias=id)

    class Config(Base_Config):
        pass