import pdb as debug
from bson import ObjectId
from Models.recomendations_model import Recomendations

debug.set_trace()
recomendations = Recomendations(
    user_id=ObjectId("66ca817906d85adc79a4de70"),
    recomended_items=[{ObjectId("66ca817906d85adc79a4de71"):4.5}]
)
print(' recomendation it is ok')