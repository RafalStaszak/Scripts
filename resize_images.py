import argparse
import cv2
import os
import numpy as np
import multiprocessing

parser = argparse.ArgumentParser()
parser.add_argument('--w', help='Target image width')
parser.add_argument('--h', help='Target image height')
parser.add_argument('--source', help='Directory containing images')
parser.add_argument('--target', help='Directory containing images')
args = parser.parse_args()

w = int(args.w)
h = int(args.h)
source = args.source
target = args.target

paths = os.listdir(source)
paths_split = np.array_split(paths, multiprocessing.cpu_count())


def process(items):
    for item in items:
        img = cv2.imread(os.path.join(source, item))
        img = cv2.resize(img, dsize=(w, h))
        cv2.imwrite(os.path.join(target, item), img)

jobs = []
for process_paths in paths_split:
    p = multiprocessing.Process(target=process, args=(process_paths,))
    jobs.append(p)
    p.start()