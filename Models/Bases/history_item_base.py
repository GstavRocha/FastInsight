from object_Id_base import Object_Id
from pydantic import BaseModel,Field

class History_Item(BaseModel):
    item_id: Object_Id = Field