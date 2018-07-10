# renameMp4
# Created by JKChang
# 04/06/2018, 10:56
# Tag:
# Description: rename all the mp4 files in the same folder

import os
import re

# path = r'/Users/jkchang/Desktop/test'
path = r'/Users/jkchang/Desktop/up'

fileCount = 51

sublist = sorted(os.listdir(path))
try:
    sublist.remove('.DS_Store')
except:
    pass

print(sublist)


def semi_num(text):
    return int(re.match(r'(\d+).(\d+)', text).group(2))

for sub in sublist:

    subpath = os.path.join(path, sub)
    txtlist = os.listdir(subpath)
    try:
        txtlist.remove('.DS_Store')
    except:
        pass

    txtlist.sort(key=semi_num)

    for txtfile in txtlist:
        file_removed = re.sub(r'\d\.\d+', '', txtfile)
        sub_removed = re.sub(r'\d*-', '', sub)
        os.rename(os.path.join(subpath, txtfile),
                  os.path.join(subpath, str(fileCount).zfill(3) + " " + sub_removed + " " + file_removed))
        fileCount += 1

