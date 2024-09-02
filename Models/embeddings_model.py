from pydantic import BaseModel, Field
from typing import Optional,Dict, List
from Models.generate_id import generate_id
from datetime import datetime

class Embeddings(BaseModel):
    id_embeddings: Optional[str] = Field(default_factory=generate_id, alias='_id')
    entity_type: str = Field(description="Ex: user, item")
    entity_id: str = Field(default_factory=generate_id)
    embedings_vector: List[float]
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    update_at: Optional[datetime] = Field(default_factory=datetime.now)
    class Config:
        arbitrary_types_allowed = True