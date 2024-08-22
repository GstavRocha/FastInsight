from pydantic import BaseModel,Field,EmailStr
from typing import Optional, List
from Models.PyObject import PyObjectId
from datetime import datetime

class User(BaseModel):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    username: str
    email: EmailStr
    peference:  List[str]=[]
    history: List[HistoryItem]=[]
    created_at: Optional[datetime]=Field(default_factory=datetime.UTC)
    updated_at: Optional[datetime]=Field(default_factory=datetime.UTC)
