from bson import ObjectId
class Config_Base:
    population_by_name = True
    json_encoders = {
        ObjectId: str
        }
    arbitrary_types_allowed = True