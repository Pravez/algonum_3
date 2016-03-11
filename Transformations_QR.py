import numpy as np
from Forme_Bidiagonale import *


def qr_transform(BD):
    n, m = BD.shape
    U = np.mat(np.identity(n))
    V = np.mat(np.identity(m))
    S = BD
    for i in range(0, 1000):
        (Q1, R1) = np.linalg.qr(np.transpose(S))
        (Q2, R2) = np.linalg.qr(np.transpose(R1))
        S = R2
        U = U * Q2
        V = np.transpose(Q1) * V
    return (U, S, V)



np.set_printoptions(5)
U, S, V = qr_transform(BD)
print(np.all(abs(U*S*V-BD)<10**(-10)))