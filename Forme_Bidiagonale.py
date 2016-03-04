import numpy as np
from Transformation_Householder import *

def getColumnFromMatrix(matrix, i, n):
    temp = np.matrix(np.zeros((n, 1)))
    for k in range (i, n):
        temp[k, 0] = matrix[k, i]
    return temp

def getRowFromMatrix(matrix, i, m):
    temp = np.mat(np.zeros((m, 1)))
    for k in range (i+1, m):
        temp[k, 0] = matrix[i, k]
    return temp

def getBidiagonal(A):
    n = len(A)
    m = len(A[0])
    BD = A
    QLeft = np.identity(n)
    QRight = np.identity(m)
#    for i in range (0, n):



print(getColumnFromMatrix(A, 1, 3))
print(getRowFromMatrix(A, 1, 3))