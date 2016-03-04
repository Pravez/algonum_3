import numpy as np


def findVector(x, y):
    num = x-y
    denom = np.linalg.norm((x-y))
    return num/denom

def householderProjection(x, y):
    u = findVector(x, y)
    n = len(x)
    return np.identity(n)-2*(np.dot(u, np.transpose(u)))

def applyHouseholderVector(x, y, u):
    n = findVector(x, y)
    return (u - 2*(np.dot(n, np.transpose(n)))*u)

def applyDumbHouseholderMatrix(m, h):
    return np.dot(m, h)

def applyOptimalHouseholderVector(x, y, u):
    n = findVector(x, y)
    return

print(applyHouseholderVector(np.matrix('[3; 4; 0.]'), np.matrix('[0; 0; 5.]'), np.matrix('[3; 4; 0.]')))