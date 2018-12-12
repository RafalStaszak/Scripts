import argparse
import os
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--source', help='Directory containing dirs')
parser.add_argument('--target', help='Directory containing dirs')
args = parser.parse_args()

source = args.source
target = args.target

paths = os.listdir(source)

files_to_move = []

for path in paths:
    path = os.path.join(source, path)
    if os.path.isdir(path):
        files_in_dir = os.listdir(path)
        for file in files_in_dir:
            shutil.move(os.path.join(path, file), os.path.join(source, file))
        os.removedirs(path)
