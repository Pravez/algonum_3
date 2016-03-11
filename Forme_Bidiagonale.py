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
    n, m = A.shape
    BD = A
    QLeft = np.mat(np.identity(n))
    QRight = np.mat(np.identity(m))
    for i in range (0, n):
        u = getColumnFromMatrix(BD, i, n)
        v = np.mat(np.zeros((n,1)))
        v[i,0] = np.linalg.norm(u)
        Q1 = householderProjection(u, v)
        QLeft = QLeft * Q1
        BD = Q1 * BD
        if i<(m-2):
            u = getRowFromMatrix(BD, i, m)
            v = np.mat(np.zeros((m,1)))
            v[i+1,0] = np.linalg.norm(u)
            Q2 = householderProjection(u, v)
            QRight = Q2 * QRight
            BD = BD * Q2
    return (QLeft,BD,QRight)



B = np.matrix('[11 21 5 12; 48 548 16 887; 47 88 91 45; 17 32 68 17]')

np.set_printoptions(precision=2)
QLeft,BD,QRight = getBidiagonal(B)