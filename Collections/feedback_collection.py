from .utils import check_and_create_collection

feedback = {
    "_id": int,
    "user_id": int,
    "feedback_type":"string", # like, deslike, rating
    "rating": float, #Caso o feedback seja um rating
    "timestamp": "datetime",
    "metadata": {"key": "value"}
}

check_and_create_collection("FEEDBACK", feedback)