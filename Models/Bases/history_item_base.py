from bson import ObjectId
from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime

class History_Item(BaseModel):
    item_id: ObjectId = Field
    timestamp: Optional[datetime] = Field()
    
    class Config:
        arbitrary_types_allowed = True
        print('history_item ok') 
        pass
        
    