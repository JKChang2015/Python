# rename md
# Created by JKChang
# 23/07/2018, 10:56
# Tag:
# Description: rename the py code to the md file in a directory

import os, sys
folder = r'/Users/jkchang/Desktop/owlready2'

for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.py','.md')
    output = os.rename(infilename,newname)