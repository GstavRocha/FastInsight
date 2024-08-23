import pdb as pd
from datetime import datetime
from user_model import User

user = User(
    username="Gustavo Rocha",
    email="nooseguitar@hotmail.com",
    preference=["tech","programming"],
    history=
        [
            {"item_id":"64d3072f4d4e3e2c2f65ef50"}
        ]
)

if __name__ =="__main__":
    pd.run(user)
