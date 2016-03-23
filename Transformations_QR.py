# -*- coding: utf-8 -*-
import numpy as np
from Forme_Bidiagonale import *
import copy

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

def qr_next_rank(U, S, V):
    (Q1, R1) = np.linalg.qr(np.transpose(S), mode='complete')  # m*m m*n
    (Q2, R2) = np.linalg.qr(np.transpose(R1), mode='complete')  # n*n n*m
    S = R2  # n*m
    U = U * Q2  # n*n
    V = np.transpose(Q1) * V  # m*m
    return (U, S, V)


def givens(a,b):
    r = np.sqrt(a*a+b*b)
    return float(a)/r, -float(b)/r


def qr_bidiag(BD):
    n,m = BD.shape
    BD2 = copy.copy(BD)

    giv_tot_2= np.mat(np.identity(n))
    for i in range(0, min(n-1,m-1)):
        cs,sn = givens(BD2[i, i], BD2[i+1, i])

        e = BD2[i, i]
        f = BD2[i+1, i]
        g = BD2[i, i+1]
        h = BD2[i+1, i+1]
        BD2[i, i] = cs*e - sn*f
        BD2[i+1,i] = 0
        BD2[i, i+1] = cs*g - sn*h
        BD2[i+1, i+1] = sn*g + cs*h

        for j in range(0,i+2):
            a,b = giv_tot_2[j, i], giv_tot_2[j, i+1]
            giv_tot_2[j,i+1] = sn*a + cs*b
            giv_tot_2[j,i] = cs*a - sn*b

    # np.set_printoptions(linewidth=150,suppress=True)
    # print(BD2)
    return giv_tot_2,BD2