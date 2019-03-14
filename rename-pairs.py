import argparse
import os
import shutil
import re


def parse_line(line):
    match = re.match(r'(\S+)\s+([0-9a-zA-Z]+)', line)
    source = match.group(1)
    target = match.group(2)
    return source, target


parser = argparse.ArgumentParser()
parser.add_argument('--dir', help='Directory containing dirs')
parser.add_argument('--pairs', help='File with pair names to change')
args = parser.parse_args()

directory = args.dir


files = os.listdir(directory)

file = args.pairs
with open(file, 'r') as f:
    contents = f.readlines()


pairs = dict()
for line in contents:
    source, target = parse_line(line)
    pairs[source] = target

for f in files:
    p = os.path.join(directory, f)
    val = pairs.get(f)
    if val is not None:
        os.rename(p, os.path.join(directory, val))
