from pydantic import BaseModel,Field
from typing import Optional,Dict,List,Union
from bson import ObjectId
from datetime import datetime

class Feedback(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='id_feedback')
    user_id: ObjectId
    item_id: ObjectId 
    feedback_type:str = Field(description="Ex: like, dislike, rating")
    rating: float = Field(description="if the feedback is a rating")
    timestamp: Optional[datetime] = Field(default_factory=datetime.now)
    metadata: Dict[str,Union[str,int,bool]]
    class Config:
        arbitrary_types_allowed = True
