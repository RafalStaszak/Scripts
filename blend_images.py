import argparse
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
from scipy.misc import imsave


def blend(x, y, overlay):
    blended = x * (1 - overlay) + y * overlay
    blended = np.clip(blended, 0.0, 1.0)
    blended = np.where(y != 0, blended, x)
    return blended


def is_mask(img):
    i = 0
    for row in img:
        for col in row:
            for px in col:
                if px != 0.0 and px != 1.0:
                    i = i + 1

    f = np.vectorize(lambda x: x == 0.0 or x == 1.0)
    non_zero = np.count_nonzero(f(img)) / 3
    total = np.shape(img)[0] * np.shape(img)[1]
    if non_zero / total > 0.98:
        return True
    else:
        return False


def replace_color(x: np.ndarray, colors):
    img = x.copy()
    for row in img:
        for px in row:
            if np.sum(px) != 0:
                px[:3] = colors[:3]

    return img


def parse_color(color: str):
    colors = color.split(',')
    return list(map(float, colors))


parser = argparse.ArgumentParser()
parser.add_argument('--img', action='append', type=str)
parser.add_argument('--out-img', type=str)
parser.add_argument('--overlay', type=float, default=0.0)
parser.add_argument('--first_color', type=str, default='1.0,0.0,0.0')
parser.add_argument('--second_color', type=str, default='0.0,1.0,0.0')

args = parser.parse_args()

one_p = list(args.img)[0]
two_p = list(args.img)[1]

img_one = imread(one_p, mode='RGB') / 255.0
img_two = imread(two_p, mode='RGB') / 255.0

if is_mask(img_one):
    img_one = replace_color(img_one, parse_color(args.first_color))

if is_mask(img_two):
    img_two = replace_color(img_two, parse_color(args.second_color))

img_out = blend(img_one, img_two, args.overlay) * 255.0

imsave(args.out_img, img_out)
