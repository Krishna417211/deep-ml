import numpy as np

def cosine_similarity(v1, v2):
	dot = np.dot(v1,v2)
	norm1 = np.linalg.norm(v1)
	norm2 = np.linalg.norm(v2)

	return dot/(norm1 * norm2)

	
	