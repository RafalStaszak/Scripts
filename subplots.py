import argparse
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
import re
from scipy.misc import imsave

def natural_sort_key(s, _nsre=re.compile('([0-9]+)')):
    return [int(text) if text.isdigit() else text.lower()
            for text in _nsre.split(s)]

parser = argparse.ArgumentParser()
parser.add_argument('--source', action='append', type=str)
parser.add_argument('--cols', type=int, default=2)

args = parser.parse_args()

source_paths = args.source

image_paths = []

for p in source_paths:
    paths = os.listdir(p)
    paths.sort(key=natural_sort_key)
    paths = [os.path.join(p, img_p) for img_p in paths]
    image_paths.extend(paths)

images = [imread(p, mode='RGB') for p in image_paths]

cols = args.cols
rows = np.ceil(len(images) / float(cols))

fig = plt.figure()
image = np.random.uniform(0.0, 1.0, (64, 64, 3))

print(cols)
print(rows)
for i in range(len(images)):
    print(i+1)
    plt.subplot(rows, cols, i+1)
    plt.imshow(images[i])
    plt.axis('off')

plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
plt.show()
