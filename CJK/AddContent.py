# AddContent
# Created by JKChang
# 12/05/2017, 09:21
# Tag:
# Description: add a line to the certain place of the document

import os


def addContent(filePath, index, content):
    f = open(filePath, "r")
    contents = f.readlines()
    f.close()

    contents.insert(index, content)

    f = open(filePath, "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()


index = 3
t = "# Tag: \n"
folderPath = '/Users/jkchang/Github/Python/100 python/'
for path, subdirs, files in os.walk(folderPath):
    for filename in files:
        if filename.endswith(('.txt', '.py', '.java')):
            filePath = os.path.join(path, filename)
            addContent(filePath,index,t)
