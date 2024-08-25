import pdb as debug
from bson import ObjectId
from Models.logs_model import Logs
debug.set_trace()

logs = Logs(
    event_type='action',
    description='test logs test',
    user_id=ObjectId("64d3072f4d4e3e2c2f65ef50"),
    item_id=ObjectId("64d3072f4d4e3e2c2f65ef16"),
    metadata={"version":1, "project_name": "analise"}
)
print('logs it is ok')
