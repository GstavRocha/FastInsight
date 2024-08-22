from pydantic import BaseModel,Field, EmailStr
from typing import Optional
from Models.PyObject import PyObjectId

class User(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    name: str 