import matplotlib.pyplot as plt
from PIL import Image
from math import cos, sin
import numpy as np


def show_results_jtm(res, title, show_results=True, save_img=False):
    # eps = np.spacing(0.0)
    # im1 = plt.pcolormesh(res, cmap=plt.cm.jet, vmin=eps)
    # plt.imshow(res, cmap=plt.cm.jet, vmin=eps)
    res_tmp = res.copy()
    res_tmp[res_tmp == 0] = 1
    plt.imshow(res_tmp, cmap=plt.cm.jet)
    plt.axis('off')
    fig = plt.gcf()
    fig.canvas.set_window_title(title)
    if save_img:
        res_tmp *= 255
        img = Image.fromarray(np.array(res_tmp, dtype=np.uint8), 'RGB')
        img.save('{}.png'.format(title))
    if show_results:
        plt.show()
    plt.close()


def draw_circle(img, x, y, rgb, image_width, image_height):
    for i in range(5):
        x_c = int(x) - 2 + i
        for j in range(5):
            y_c = int(y) - 2 + j
            if 0 < y_c < image_height and 0 < x_c < image_width:
                img[y_c, x_c] = rgb

    if 0 < y - 1 < image_height and 0 < x - 3 < image_width:
        img[y - 1, x - 3] = rgb
    if 0 < y < image_height and 0 < x - 3 < image_width:
        img[y, x - 3] = rgb
    if 0 < y + 1 < image_height and 0 < x - 3 < image_width:
        img[y + 1, x - 3] = rgb
    if 0 < y - 1 < image_height and 0 < x + 3 < image_width:
        img[y - 1, x + 3] = rgb
    if 0 < y < image_height and 0 < x + 3 < image_width:
        img[y, x + 3] = rgb
    if 0 < y + 1 < image_height and 0 < x + 3 < image_width:
        img[y + 1, x + 3] = rgb

    if 0 < y - 3 < image_height and 0 < x - 1 < image_width:
        img[y - 3, x - 1] = rgb
    if 0 < y - 3 < image_height and 0 < x < image_width:
        img[y - 3, x] = rgb
    if 0 < y - 3 < image_height and 0 < x + 1 < image_width:
        img[y - 3, x + 1] = rgb
    if 0 < y - 3 < image_height and 0 < x - 1 < image_width:
        img[y - 3, x - 1] = rgb
    if 0 < y - 3 < image_height and 0 < x < image_width:
        img[y - 3, x] = rgb
    if 0 < y - 3 < image_height and 0 < x + 1 < image_width:
        img[y - 3, x + 1] = rgb


def rotate(coordinates, phi, theta):
    x, y, z = coordinates
    transposed_coordinates = np.array([x, y, z, 1]).transpose()
    return np.array(np.matmul(np.matmul(T_r_y(phi, z), T_r_x(theta, z)), transposed_coordinates)[:3])


T_r_x = lambda phi, z: np.array(
    [
        [1, 0, 0, 0],
        [0, cos(phi), -sin(phi), 0],
        [0, sin(phi), cos(phi), 0],
        [0, 0, 0, 1]
    ]
)

T_r_y = lambda theta, z: np.array(
    [
        [cos(theta), 0, sin(theta), 0],
        [0, 1, 0, 0],
        [-sin(theta), 0, cos(theta), 0],
        [0, 0, 0, 1]
    ]
)
