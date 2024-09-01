from pydantic import BaseModel, Field
from typing import Optional,Dict,Union
from datetime import datetime
from Models.generate_id import generate_id

class Interactions(BaseModel):
    id: Optional[str] = Field(default_factory=generate_id, alias='id_iterractions')
    user_id: str
    item_id: str
    interactions_tipe: str
    timestamp: Optional[datetime]= Field(default_factory=datetime.now)
    metadata: Optional[Dict[str, Union[str,int,bool]]] = Field(default_factory=list)
    class Config:
        arbitrary_types_allowed = True
    
    
    # id user eb3ff966-226b-4a3a-9620-61d3c8e6fe92
    #id item bed6ed09-1a7b-428d-a3c7-c401edf2a00c