import pdb
from datetime import datetime
from .user_model import User

user = User(
    username="Gustavo Rocha",
    email="nooseguitar",
    preference=["tech","programming"],
    history=
        [
            {"item_id":"64d3072f4d4e3e2c2f65ef50","timestamp": datetime.UTC}
        ]
)
print(user)