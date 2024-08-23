from bson import ObjectId
class Base_Config:
    population_by_name = True
    json_encoders = {ObjectId: str}
    arbitrary_types_allowed = True