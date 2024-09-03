from pydantic import BaseModel, Field
from typing import Optional,Dict,List
from Models.generate_id import generate_id
from datetime import datetime

class Recomendations(BaseModel):
    id_recomendation: Optional[str] = Field(default_factory=generate_id, alias="_id")
    user_id:str
    recomended_items: List[Dict[str,float]]
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    class Config:
        arbitrary_types_allowed = True