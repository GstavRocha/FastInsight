from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from Models.user_model import User

class User_Embeddings(BaseModel):
    user_id: str = Field(default=User.id,alias='id')
    embedding_vector: List[float]
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    class Config:
        arbitrary_types_allowed = True