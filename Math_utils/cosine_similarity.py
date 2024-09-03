import numpy as np

def cosine_similarity(vector1, vector2):
    dot_product = np.dot(vector1,vector2)
    normative_vector1 = np.linalg.norm(vector1)
    normative_vector2= np.linalg.norm(vector2)
    similarity = dot_product/(normative_vector1 * normative_vector2)
    print(similarity)
    return similarity
