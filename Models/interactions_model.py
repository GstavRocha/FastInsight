from pydantic import BaseModel, Field
from typing import Optional,Dict,Union
from bson import ObjectId
from datetime import datetime

class Interactions(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='id_iterractions')
    user_id: ObjectId
    item_id: ObjectId
    interactions_tipe: str
    timestamp: Optional[datetime]= Field(default_factory=datetime.now)
    metadata: Dict[str, Union[str,int,bool]]
    class Config:
        arbitrary_types_allowed = True
    