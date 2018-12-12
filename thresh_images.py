import argparse
import cv2
import os

parser = argparse.ArgumentParser()
parser.add_argument('--source', help='Directory containing images')
parser.add_argument('--target', help='Directory containing images')
parser.add_argument('--thresh', help='Thresh value')
args = parser.parse_args()

source = args.source
target = args.target
thresh = int(args.thresh)

paths = os.listdir(source)
for path in paths:
    img = cv2.imread(os.path.join(source, path), cv2.IMREAD_GRAYSCALE)
    _, img = cv2.threshold(img, thresh, 255, type=cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(target, path), img)
