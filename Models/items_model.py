from pydantic import BaseModel,Field
from typing import Optional,List,Dict,Union
from datetime import datetime
from bson import ObjectId

class Items(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='id_items')
    name: str
    description: str
    category: str
    tags: List[Dict[str,str]]
    metadata: Dict['str', Union[str,int,bool]]
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    
    class Config:
        arbitrary_types_allowed = True
    
    
    