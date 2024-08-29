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
           {1: datetime.now()}
        ]

)
print('teste user is ok')
print(user)
