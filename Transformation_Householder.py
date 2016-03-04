import numpy as np


def findUVector(x, y):
    num = x-y
    denom = np.linalg.norm((x-y))
    return num/denom

def householderProjection(x, y):
    u = findUVector(x, y)
    n = len(x)
    return np.identity(n)-2*(np.dot(u, np.transpose(u)))

print(householderProjection(np.matrix('[3; 4; 0.]'), np.matrix('[0; 0; 5.]')))