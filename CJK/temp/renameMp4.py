# renameMp4
# Created by JKChang
# 04/06/2018, 10:56
# Tag:
# Description: rename all the mp4 files in the same folder

import os
import re

# path = r'/Users/jkchang/Desktop/test'
path = r'/Users/jkchang/Desktop/untitled folder'

fileCount = 1

sublist = sorted(os.listdir(path))
try:
    sublist.remove('.DS_Store')
except:
    pass

for sub in sublist:

    subpath = os.path.join(path, sub)
    txtlist = sorted(os.listdir(subpath))
    try:
        txtlist.remove('.DS_Store')
    except:
        pass

    for txtfile in txtlist:
        file_removed = re.sub(r'\d\.\d', '', txtfile)
        sub_removed = re.sub(r'\d*-', '', sub)
        os.rename(os.path.join(subpath, txtfile),
                  os.path.join(subpath, str(fileCount).zfill(3) + " " + sub_removed + " " + file_removed))
        fileCount += 1
