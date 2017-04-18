# -*- coding: utf-8 -*-

import glob
import os
import sys

ROOT_DIR=sys.argv[1]

file_list = glob.glob(ROOT_DIR + '*/*.py')
for f in file_list:
    _f = f.split(os.sep)
    print(_f[-2] + '->' + _f[-1])


# import os
# files = os.listdir(ROOT_DIR)
#  
# for file in files:
#     print(file)

