import shutil
import os
import sys
target = sys.argv[1]
for root, dirs, files in os.walk(target):
    for val in files:
        if  not (val.endswith('jpg') or  val.endswith('csv')  or val.endswith('js') or val.endswith('css') \
                 or val.endswith('png') \
                or val.endswith('html')):
            val = root + '/' + val
            print(val)
            os.remove(val)
