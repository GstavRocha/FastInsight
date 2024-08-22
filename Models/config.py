from bson import ObjectId
class Base_Config:
    allow_population_by_field_name = True
    json_encoders = {ObjectId: str}
    arbitrary_types_allowed = True