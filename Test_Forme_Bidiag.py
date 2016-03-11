# -*- coding: utf-8 -*-
from Forme_Bidiagonale import *
import unittest

def repeat(times):
    # Trouvé sur internet. Permet de répéter times fois un test unitaire
    def repeatHelper(f):
        def callHelper(*args):
            for i in range(0, times):
                f(*args)
        return callHelper
    return repeatHelper


class TestBidiagonal(unittest.TestCase):

    def test_bidiag_prev(self):
        B = np.matrix('[11 21 5 12; 48 548 16 887; 47 88 91 45; 17 32 68 17]')
        n, m = 3, 3
        QLeft, BD, QRight = getBidiagonal(B)
        produit = QLeft * BD * QRight

        # test décomposition
        for i in range(0, n):
            for j in range(0, m):
                self.assertAlmostEquals(B[i, j], produit[i, j])

        # test QLeft et QRight orthogonales
        QL = QLeft * np.transpose(QLeft)
        QR = QRight * np.transpose(QRight)
        for i in range(0, n):
            for j in range(0, n):
                if i==j:
                    self.assertAlmostEquals(1, QL[i, j])
                else:
                    self.assertAlmostEquals(0, QL[i, j])
        for i in range(0, m):
            for j in range(0, m):
                if i==j:
                    self.assertAlmostEquals(1, QR[i, j])
                else:
                    self.assertAlmostEquals(0, QR[i, j])

        # test BD bidiag
        for i in range(0,n):
            for j in range(0,m):
                if i>j or i<j-1:
                    self.assertAlmostEquals(BD[i,j],0)

if __name__ == '__main__':
    unittest.main()