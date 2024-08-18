from .utils import check_and_create_collection

embeddings = {
    "_id": "ObjectId",
    "entity_type": "string", #EX user, itme
    "entity_id": "objectId",    
    "embedding_vector":["float"],
    "created_at": "datetime",
    "updated_at": "datetime"
}

check_and_create_collection("EMBEDDINGS", embeddings)