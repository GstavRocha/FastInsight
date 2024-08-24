import pdb as debug
from bson import ObjectId
from datetime import datetime
from Models.interactions_model import Interactions

debug.set_trace()
interaction = Interactions(
    user_id = ObjectId("64d3072f4d4e3e2c2f65ef51"),
    item_id = ObjectId("64d3072f4d4e3e2c2f65ef50"),
    interactions_tipe = 'mouse',
    metadata = [
        {"action": "teste", "meta":"teste1"}
    ]
)
print('Interraction it is ok')
