# -*- coding: utf-8 -*-
import numpy as np
from Forme_Bidiagonale import *
import matplotlib.pyplot as plt

np.set_printoptions(linewidth=200)


def qr_transform(BD, NMax):
    n, m = BD.shape
    U = np.mat(np.identity(n))
    V = np.mat(np.identity(m))
    S = BD  # n*m
    for i in range(0, NMax):
        (Q1, R1) = np.linalg.qr(np.transpose(S), mode='complete')  # m*m m*n
        (Q2, R2) = np.linalg.qr(np.transpose(R1), mode='complete')  # n*n n*m
        S = R2  # n*m
        U = U * Q2  # n*n
        V = np.transpose(Q1) * V  # m*m
    return (U, S, V)