# import numpy as np
# from datetime import datetime
# from Database.connection import db_conn,db_off
# from fastapi import HTTPException

# def generate_user_embedding(user_id: str):
#     database=db_conn()
#     user_collection=database["User_Embeddings"]
#     item_collection=database["Item_Embeddings"]
#     user_embedding = user_collection.find_one({"user_id":user_id})
#     if not user_embedding:
#         raise HTTPException(status_code=404,detail="User embedding not found")
    
#     user_vector=user_embedding["embedding_vector"]
#     recommendation = []
#     for item in item_collection.find():
        
        