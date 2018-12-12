import os
import cv2
import numpy as np
from tqdm import tqdm

mask_path = '/home/rafal/Datasets/6dposes_dataset/train_aruco/aruco_dark/mask'
rgb_path = '/home/rafal/Datasets/6dposes_dataset/train_aruco/aruco_dark/rgb'
bg_path = '/home/rafal/Datasets/sample_backgrounds/training'

masks = os.listdir(mask_path)
rgbs = os.listdir(rgb_path)
bgs = os.listdir(bg_path)

masks.sort()
rgbs.sort()
bgs.sort()


def swap_background(rgb, mask, bg):
    bg = cv2.resize(bg, rgb.shape[:2])
    h, w = rgb.shape[:2]
    for i in range(h):
        for j in range(w):
            if mask[i, j] == 0:
                rgb[i, j] = bg[i, j]

    return rgb


for rgb_file, mask_file in tqdm(zip(rgbs, masks), total=len(rgbs)):
    rgb_img = cv2.imread(os.path.join(rgb_path, rgb_file))
    mask_img = cv2.imread(os.path.join(mask_path, mask_file), cv2.IMREAD_GRAYSCALE) / 255
    bg_img = cv2.imread(os.path.join(bg_path, np.random.choice(bgs)))

    result = swap_background(rgb_img, mask_img, bg_img)
    cv2.imwrite(os.path.join(rgb_path, rgb_file), result)
