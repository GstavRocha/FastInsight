from pydantic import BaseModel,Field
from typing import Dict, Union, Optional
from bson import ObjectId
from datetime import datetime

class Models(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='id_models')
    model_name: str
    version: str
    trained_at: Optional[datetime] = Field(default_factory=datetime.now)
    metadata: Dict[str, Union[str,int,bool]]
    class Config:
        arbitrary_types_allowed = True
        

