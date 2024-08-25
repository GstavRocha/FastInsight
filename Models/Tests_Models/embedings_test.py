import pdb as debug
from bson import ObjectId
from Models.embeddings_model import Embedings
debug.set_trace()
embedings = Embedings(
    entity_type='item teste',
    entity_id=ObjectId('64d3072f4d4e3e2c2f65ef50'),
    embedings_vector=8.0
)
print(embedings)
print("embeding on test")