from pydantic import BaseModel,Field
from typing import Optional,List,Dict,Union
from datetime import datetime
from Models.generate_id import generate_id

class Items(BaseModel):
    id_items: Optional[str] = Field(default_factory=generate_id, alias='_id')
    name: str
    description: str
    category: str
    tags: List[str]
    metadata: Optional[Dict[str, Union[str,int,bool]]] = Field(default_factory=list)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    
    class Config:
        arbitrary_types_allowed = True
    
    
    