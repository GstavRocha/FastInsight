from Bases.object_Id_base import Object_Id
from pydantic import BaseModel,Field
from typing import Optional
from datetime import time

class History_Item(BaseModel):
    item_id: Object_Id = Field
    timestamp: Optional = File