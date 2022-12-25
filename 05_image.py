import imageio.v2 as iio
import matplotlib.pyplot as plt
import numpy as np

shape = (16, 16)
dtype = np.uint8


def show_img(img):
    plt.imshow(img, cmap="gray")
    plt.show()


def black_img():
    img = np.zeros(shape, dtype=dtype)
    return img


def noisy_img():
    img = np.random.normal(128, 64, size=shape)
    return img


def cross():
    img = black_img()
    for i in range(shape[0]):
        img[10, i] = 128
        img[i, 10] = 255

    return img


def cameraman():
    img = iio.imread("cameraman.tif")
    return img


def downscale(img):
    downscale_factor = int(img.shape[0]/shape[0]), int(img.shape[1]/shape[1])
    img = img[::downscale_factor[0], ::downscale_factor[1]]
    return img


def remove_diagonal(img):
    for i in range(img.shape[0]):
        img[i, i] = 0
    return img


img = black_img()
img = cameraman()
img = downscale(img)
img = remove_diagonal(img)

show_img(img)
