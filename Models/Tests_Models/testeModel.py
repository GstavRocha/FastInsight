import pdb as debugger
from Models.user_model import User
from bson import ObjectId
from datetime import datetime
debugger.set_trace()
user = User(
    username="Gustavo Rocha",
    email="nooseguitar@hotmail.com",
    preference=["tech","programming"],
    history=
        [
           {ObjectId("64d3072f4d4e3e2c2f65ef50"): datetime.now()}
        ]

)
print('teste user is ok')
print(user)
