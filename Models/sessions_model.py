from pydantic import BaseModel,Field
from typing import Optional,Dict,Union
from bson import ObjectId
from datetime import datetime

class Sessions(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias="id_session")
    user_id: ObjectId
    session_start:Optional[datetime] = Field(default_factory=datetime.now)
    session_end:Optional[datetime]= Field(default_factory=datetime.now)
    location: str
    metadata: Dict[str, Union[str, int, bool]]
    class Config:
        arbitrary_types_allowed = True