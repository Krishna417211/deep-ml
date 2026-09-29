import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    if norm_type == 'l1':
        if arr.shape == (2,2):
            return np.linalg.norm(arr.flatten(), ord = 1)
        else:
            return np.linalg.norm(arr, ord = 1)


    elif norm_type == 'l2':
        if arr.shape == (2,2):
            return np.linalg.norm(arr.flatten(), ord = 2)
        else:
            return np.linalg.norm(arr, ord = 2)

    elif norm_type == 'linf':
        if arr.shape == (2,2):
            return np.linalg.norm(arr.flatten(), ord = np.inf)
        else:
            return np.linalg.norm(arr, ord = np.inf)

    elif norm_type == 'frobenius':
        return np.linalg.norm(arr, ord = 'fro')

    else:
        return None

     # Your code here
  
