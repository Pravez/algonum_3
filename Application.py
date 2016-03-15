import matplotlib
from scipy import misc

from Transformations_QR import *



def compress_rank_k(S, k):
    n, m = S.shape
    for i in range(k, min(n, m)-1):
        S[i, i] = 0

    return S

#define region
def get_pixels_from_color(image, pix):
    n, m, s = image.shape
    ret = np.mat(np.zeros((n, m)))
    for i in range(0, n):
        for j in range(0, m):
            ret[i, j] = image[i][j][pix]

    return ret

def normalize_pixel(pix):
    if(pix[0] > 255):
        pix[0] = 255
    if(pix[1] > 255):
        pix[1] = 255
    if(pix[2] > 255):
        pix[2] = 255
    return pix

def apply_compression(matrix, compression_rate, qr_rate):
    QL, BD, QR = getBidiagonal(matrix)
    U, S, V = qr_transform(BD, qr_rate)
    S = compress_rank_k(S, compression_rate)

    return QL*U*S*V*QR

def reconstitute_image(red, green, blue):
    n, m = red.shape
    res = np.zeros((n, m, 3), dtype="uint8")
    for i in range(0, n):
        for j in range(0, m):
            res[i][j] = normalize_pixel([red[i, j], green[i, j], blue[i, j]])

    return res

def Compress_Image(image):
    img = misc.imread(image)
    qr_rate = 20
    compression_rate = 30

    red = get_pixels_from_color(img, 0)
    green = get_pixels_from_color(img, 1)
    blue = get_pixels_from_color(img, 2)

    red_c = apply_compression(red, compression_rate, qr_rate)
    green_c = apply_compression(green, compression_rate, qr_rate)
    blue_c = apply_compression(blue, compression_rate, qr_rate)

    image_compressed = reconstitute_image(red_c, green_c, blue_c)

    plt.imshow(image_compressed)
    plt.show()

Compress_Image("p3_takeoff_base.png")