from pydantic import BaseModel, Field
from typing import Optional,Dict,List
from bson import ObjectId
from datetime import datetime

class Recomendations(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias="id_recomendation")
    user_id:ObjectId
    recomended_items: List[Dict[ObjectId,float]]
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    class Config:
        arbitrary_types_allowed = True
print("recomendations on test")