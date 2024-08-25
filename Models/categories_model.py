from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId
from datetime import datetime

class Categories(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias='id_categories')
    category_name: str
    parent_category:Optional[ObjectId]= Field(default_factory=ObjectId, description= "For Subcategories")
    created_at: Optional[datetime]=Field(default_factory=datetime.now)
    update_at: Optional[datetime]=Field(default_factory=datetime.now)

    class Config:
        arbitrary_types_allowed= True


