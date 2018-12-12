import os
import imghdr
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--source', help='Directory containing dirs')
parser.add_argument('--target', help='Directory containing dirs')
args = parser.parse_args()

source = args.source
target = args.target

i = 0
files = os.listdir(source)
files.sort()

for file in files:
    if imghdr.what(os.path.join(source, file)) == 'jpeg':
        old_file = os.path.join(source, file)
        new_file = os.path.join(target, '{0}.jpg'.format(i))
        os.rename(old_file, new_file)
        i = i + 1
    else:
        os.remove(os.path.join(source, file))
        print(file)

    
