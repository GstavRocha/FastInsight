import pdb as debugger
from pydantic import BaseModel
from Models.sessions_model import Sessions
from bson import ObjectId
sessions = Sessions(
    user_id=ObjectId("66ca817906d85adc79a4de70"),
    location="parnamirim",
    # metadata=[{"action": "teste", "meta1": "teste1"}] 
)   
print(sessions)