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


#define region
def getPixels(image, pix):
    n, m, s = image.shape
    ret = np.mat(np.zeros((n, m)))
    for i in range(0, n):
        for j in range(0, m):
            ret[i, j] = image[i][j][pix]

    return ret

def reconstitute_image(red, green, blue):
    n, m = red.shape
    res = np.zeros((n, m, 3), dtype="uint8")
    for i in range(0, n):
        for j in range(0, m):
            if(red[i, j] > 255):
                red[i, j] = 255
            if(green[i, j] > 255):
                green[i, j] = 255
            if(blue[i, j] > 255):
                blue[i, j] = 255
            res[i][j][0] = red[i, j]
            res[i][j][1] = green[i, j]
            res[i][j][2] = blue[i, j]

    return res

def apply_compression(matrix):
    QL, BD, QR = getBidiagonal(matrix)
    U, S, V = qr_transform(BD, 20)
    S = remove_on_diag(S, 30)

    return QL*U*S*V*QR

def Apply_to_image(image):
    img = misc.imread(image)

    red = getPixels(img, 0)
    green = getPixels(img, 1)
    blue = getPixels(img, 2)

    red_c = apply_compression(red)
    green_c = apply_compression(green)
    blue_c = apply_compression(blue)

    rec = reconstitute_image(red_c, green_c, blue_c)
    #print(rec)

    plt.imshow(rec)
    plt.show()


def Apply_to_image_with_gs(image):
    img = misc.imread(image)

    grey = np.zeros((img.shape[0], img.shape[1])) # init 2D numpy array
    # get row number
    for rownum in range(len(img)):
       for colnum in range(len(img[rownum])):
          grey[rownum][colnum] = average(img[rownum][colnum])

    grey = np.matrix(grey)
    QL, BD, QR = getBidiagonal(grey)
    U, S, V = qr_transform(BD, 20)
    S = remove_on_diag(S, 10)

    rec = QL*U*S*V*QR
    plt.imshow(rec, cmap = matplotlib.cm.Greys_r)
    plt.show()

Apply_to_image("p3_takeoff_base.png")