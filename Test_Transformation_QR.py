# -*- coding: utf-8 -*-
import unittest
from Transformations_QR import *
import matplotlib.pyplot as plt
import random

def repeat(times):
    # Trouvé sur internet. Permet de répéter times fois un test unitaire
    def repeatHelper(f):
        def callHelper(*args):
            for i in range(0, times):
                f(*args)
        return callHelper
    return repeatHelper

class TestQRTransform(unittest.TestCase):

    @repeat(1)
    def test_QR_Converge(self):
        NB = 50
        n, m = random.randint(5, 50), random.randint(5, 50)
        n,m = 90, 90
        B = np.mat(255*np.random.rand(n, m))
        QLeft, BD, QRight = getBidiagonal(B)

        iter = [i for i in range(1, NB)]
        conv = [0 for i in range(1, NB)]

        U,S,V = qr_transform(BD, 1)

        for k in range(1, NB):
            U, S, V = qr_next_rank(U, S, V)
            produit = U*S*V
            for i in range(0, n):
                for j in range(0, m):
                    self.assertAlmostEquals(BD[i, j], produit[i, j])
                    if(i<>j and abs(S[i, j])>epsilon):
                        conv[k-1]+=1

        # plt.plot(iter, conv)
        # plt.ylabel("Nombre de termes extradiagonaux non nuls")
        # plt.xlabel("Nombre d'iterations")
        # plt.show()


    @repeat(50)
    def test_qr_bidiag(self):
        NB = 50
        n,m=0,1
        while n<m:
            n, m = random.randint(5, 50), random.randint(5, 50)
        # n,m = 90, 90
        B = np.mat(255*np.random.rand(n, m))
        QLeft, BD, QRight = getBidiagonal(B)

        Q,R = qr_bidiag(np.transpose(BD))

        produit = Q * R

        # test décomposition
        for i in range(0, m):
            for j in range(0, n):
                self.assertAlmostEquals(BD[j, i], produit[i, j])

        # test Q orthogonale
        QO = Q * np.transpose(Q)
        for i in range(0, m):
            for j in range(0, m):
                if i==j:
                    self.assertAlmostEquals(1, QO[i, j])
                else:
                    self.assertAlmostEquals(0, QO[i, j])

        # test R bidiag
        for i in range(0,m):
            for j in range(0,n):
                if i>j or i<j-1:
                    self.assertAlmostEquals(R[i,j],0)

if __name__ == '__main__':
    unittest.main()