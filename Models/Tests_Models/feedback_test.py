import pdb as debug
from bson import ObjectId
from Models.feedback_model import Feedback

debug.set_trace()
feedback = Feedback(
    user_id=ObjectId('64d3072f4d4e3e2c2f65ef50'),
    item_id=ObjectId('64d3072f4d4e3e2c2f65ef52'),
    feedback_type="like",
    rating=2.0,
    metadata={"version":1, "project_name": "analise"}
)
print(feedback)
print('feedback_test it is ok')
