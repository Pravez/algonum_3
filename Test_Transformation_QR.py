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
        np.set_printoptions(linewidth=200)
        NB = 50
        n, m = random.randint(5, 50), random.randint(5, 50)
        n,m = 100, 100
        B = np.mat(1000*np.random.rand(n, m))
        QLeft, BD, QRight = getBidiagonal(B)

        iter = [i for i in range(1, NB)]
        conv = [0 for i in range(1, NB)]

        for k in range(1, NB):
            U, S, V = qr_transform(BD, k)
            produit = U*S*V
            for i in range(0, n):
                for j in range(0, m):

                    self.assertAlmostEquals(BD[i, j], produit[i, j])
                    if(i<>j and abs(S[i, j])>epsilon):
                        conv[k-1]+=1

        plt.plot(iter, conv)
        plt.show()



n,m = 100, 100
B = np.mat(10*np.random.rand(n, m))
QLeft, BD, QRight = getBidiagonal(B)

BD=np.transpose(BD)
a = time.clock()
qr_bidiag(BD)
b = time.clock()
print(b-a)
np.linalg.qr(BD,mode='complete')
print(time.clock()-b)

if __name__ == '__main__':
    unittest.main()