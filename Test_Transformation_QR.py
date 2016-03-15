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

    @repeat(50)
    def test_QR_Converge(self):
        n, m = random.randint(5,10), random.randint(5,10)
        B = np.mat(100*np.random.rand(n, m))
        print(B.shape)
        QLeft, BD, QRight = getBidiagonal(B)
        print(BD.shape)

        iter = [i for i in range(1, 50)]
        conv = [0 for i in range(1, 50)]

        for k in range(1, 50):
            U, S, V = qr_transform(BD, k)
            print(S.shape)
            print("\n")
            produit = U*S*V
            for i in range(0, n):
                for j in range(0, m):

                    self.assertAlmostEquals(BD[i, j], produit[i, j])
                    if(i<>j and abs(S[i, j])>epsilon):
                        conv[k-1]+=1

        # plt.plot(iter, conv)
        # plt.show()

if __name__ == '__main__':
    unittest.main()