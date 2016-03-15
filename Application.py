import matplotlib.image as mimg
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pylab
from scipy import misc

from Transformations_QR import *
from Transformation_Householder import *
from Forme_Bidiagonale import *


def average(pixel):
    return (pixel[0]*0.299 + pixel[1]*0.587 + pixel[2]*0.114)/3

def remove_on_diag(S, k):
    n, m = S.shape
    for i in range(k, min(n, m)):
        S[i, i] = 0

    return S

def Apply_to_image(image):
    img = misc.imread(image, 0)

    grey = np.zeros((img.shape[0], img.shape[1])) # init 2D numpy array
    # get row number
    for rownum in range(len(img)):
       for colnum in range(len(img[rownum])):
          grey[rownum][colnum] = average(img[rownum][colnum])

    grey = np.matrix(grey)
    QL, BD, QR = getBidiagonal(grey)
    U, S, V = qr_transform(BD, 20)
    S = remove_on_diag(S, 10)

    plt.imshow(U*S*V, cmap = matplotlib.cm.Greys_r)
    plt.show()

Apply_to_image("p3_takeoff_base.png")