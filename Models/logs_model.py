from pydantic import BaseModel, Field
from typing import Dict,Optional, Union
from bson import ObjectId
from datetime import datetime
class Logs(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='id_logs')
    event_type: str
    description: str
    user_id: ObjectId
    item_id: ObjectId
    timestamp: Optional[datetime] = Field(default_factory=datetime.now)
    metadata: Dict[str,Union[str,int,bool]]
    class Config:
        arbitrary_types_allowed = True
