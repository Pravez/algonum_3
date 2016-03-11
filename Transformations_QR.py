import numpy as np
from Forme_Bidiagonale import *


def qr_transform(BD):
    n = A.shape[0]
    m = A.shape[1]
    U = np.mat(np.identity(n))
    V = np.mat(np.identity(m))
    S = BD
    for i in range(0, 10**6):
        (Q1, R1) = np.linalg.qr(np.transpose(S))
        (Q2, R2) = np.linalg.qr(np.transpose(R1))
        S = R2
        U = U * Q2
        V = np.transpose(Q1) * V
    return (U, S, V)