import pdb as debugger
from Models.items_model import Items

debugger.set_trace()
items = Items(
    name='brincar',
    description='brinquedos',
    category='modelo',
    tags=[
        {"action": "add_tag", "tag": "python"},
        {"action": "add_tag", "tag": "pandas"}
    ],
    metadata={"version": 1, "project_name": "AnaliseData"}
)
print(items)