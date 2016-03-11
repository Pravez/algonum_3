import numpy as np
from Forme_Bidiagonale import *
import matplotlib.pyplot as plt


def qr_transform(BD, NMax):
    n, m = BD.shape
    U = np.mat(np.identity(n))
    V = np.mat(np.identity(m))
    S = BD
    for i in range(0, NMax):
        (Q1, R1) = np.linalg.qr(np.transpose(S))
        (Q2, R2) = np.linalg.qr(np.transpose(R1))
        S = R2
        U = U * Q2
        V = np.transpose(Q1) * V
    return (U, S, V)


np.set_printoptions(1, suppress=True)
B = np.mat(100*np.random.rand(10, 10))
QLeft, BD, QRight = getBidiagonal(B)

iter = [i for i in range(1, 50)]
conv = [0 for i in range(1, 50)]

for i in range(1, 50):
    U, S, V = qr_transform(BD, i)

    for j in range(0, 10):
        for k in range(0, 10):
            if(j<>k and abs(S[j, k])>epsilon):
                conv[i-1]+=1
plt.plot(iter, conv)
plt.show()