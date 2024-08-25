from pydantic import BaseModel, Field
from typing import Optional,Dict, List
from bson import ObjectId
from datetime import datetime

class Embedings(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='id_embedings')
    entity_type: str = Field(description="Ex: user, item")
    entity_id:ObjectId
    embedings_vector: float
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    update_at: Optional[datetime] = Field(default_factory=datetime.now)
    class Config:
        arbitrary_types_allowed = True