import matplotlib as mp
import copy
from Transformations_QR import *

def compress_rank_k(S, k):
    n, m = S.shape
    SS = copy.copy(S)
    for i in range(k, min(n, m)-1):
        SS[i, i] = 0

    return SS

#define region
def get_pixels_from_color(image, pix):
    n, m, s = image.shape
    ret = np.mat(np.zeros((n, m)))
    for i in range(0, n):
        for j in range(0, m):
            ret[i, j] = image[i][j][pix]

    return ret

def normalize_pixel(pix):
    if(pix[0] > 1.0):
        pix[0] = 1.0
    if(pix[0] < 0.0):
        pix[0] = 0.0
    if(pix[1] > 1.0):
        pix[1] = 1.0
    if(pix[1] < 0.0):
        pix[1] = 0.0
    if(pix[2] > 1.0):
        pix[2] = 1.0
    if(pix[2] < 0.0):
        pix[2] = 0.0
    return pix

def colors_bidiag_qr(red, green, blue, qr_rate):
    #on les stocke de maniere globale, pour eviter d'avoir a les recalculer plusieurs fois
    QL, BD, QR = getBidiagonal(red)
    red_tuple = (QL, qr_transform(BD, qr_rate), QR)

    QL, BD, QR = getBidiagonal(green)
    green_tuple = (QL, qr_transform(BD, qr_rate), QR)

    QL, BD, QR = getBidiagonal(blue)
    blue_tuple = (QL, qr_transform(BD, qr_rate), QR)

    return (red_tuple, green_tuple, blue_tuple)

def apply_compression(color, compression_rate):
    S = compress_rank_k(color[1][1], compression_rate)

    #QL*U*S*V*QR
    return color[0]*color[1][0]*S*color[1][2]*color[2]

def reconstitute_image(red, green, blue):
    n, m = red.shape
    res = np.zeros((n, m, 3), dtype="float32")
    for i in range(0, n):
        for j in range(0, m):
            res[i][j] = normalize_pixel([red[i, j], green[i, j], blue[i, j]])

    return res

def Compress_Image(array, cr):

    red_co = apply_compression(array[0], cr)
    green_co = apply_compression(array[1], cr)
    blue_co = apply_compression(array[2], cr)

    image_compressed = reconstitute_image(red_co, green_co, blue_co)

    return image_compressed

def measure_effectiveness(image1, image2):
    return np.linalg.norm(image1 - image2)

def create_effectiveness(image):
    img = mp.image.imread(image)

    print("Getting each pixel's matrix ...")
    red = get_pixels_from_color(img, 0)
    green = get_pixels_from_color(img, 1)
    blue = get_pixels_from_color(img, 2)

    print("Getting bidiagonals and applying qr ...")
    (red_tuple, green_tuple, blue_tuple) = colors_bidiag_qr(red, green, blue, qr_rate)
    array_colors = []
    array_colors.append(red_tuple)
    array_colors.append(green_tuple)
    array_colors.append(blue_tuple)

    print("Measuring effectiveness ...")
    eff = []
    for i in range(0, 200):
        print("rank "+`i`+"...")
        eff.append(measure_effectiveness(img, Compress_Image(array_colors, i)))

    iter = [i for i in range (0, 200)]

    plt.plot(iter, eff)
    plt.ylabel("Distance entre les matrices")
    plt.xlabel("Compression au rang k")
    plt.show()

def get_Compressed_image(image, compression_rate):
    img = mp.image.imread(image)

    red = get_pixels_from_color(img, 0)
    green = get_pixels_from_color(img, 1)
    blue = get_pixels_from_color(img, 2)

    (red_tuple, green_tuple, blue_tuple) = colors_bidiag_qr(red, green, blue, qr_rate)
    array_colors = []
    array_colors.append(red_tuple)
    array_colors.append(green_tuple)
    array_colors.append(blue_tuple)

    plt.imshow(Compress_Image(array_colors, compression_rate))
    plt.show()


qr_rate = 20

#get compressed image with certain compression rate
##get_Compressed_image("p3_takeoff_base.png", 50)
#get effectiveness
create_effectiveness("p3_takeoff_base.png")