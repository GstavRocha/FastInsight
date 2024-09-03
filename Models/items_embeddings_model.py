from pydantic import BaseModel, Field
from typing import Optional,Dict,List
from Models.generate_id import generate_id
from datetime import datetime
class Item_Embeddings(BaseModel):
    id_embedding: Optional[str] = Field(default_factory=generate_id, alias='_id')
    item_id: str
    item_name: str
    embedding_vector: List[float]
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    
    class Config:
        arbitrary_types_allowed = True