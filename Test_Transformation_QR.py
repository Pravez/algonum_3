import numpy as np
import unittest
from Transformations_QR import *
import matplotlib.pyplot as plt

class TestQRTransform(unittest.TestCase):

    def QR_Converge(self):
        np.set_printoptions(1, suppress=True)
        B = np.mat(100*np.random.rand(10, 10))
        QLeft, BD, QRight = getBidiagonal(B)

        iter = [i for i in range(1, 50)]
        conv = [0 for i in range(1, 50)]

        for i in range(1, 50):
            U, S, V = qr_transform(BD, i)
            assert(np.all(abs(U*S*V - BD) < epsilon))

            for j in range(0, 10):
                for k in range(0, 10):
                    if(j<>k and abs(S[j, k])>epsilon):
                        conv[i]+=1
        plt.plot(iter, conv)
        plt.show()

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
                conv[i]+=1
plt.plot(iter, conv)
plt.show()