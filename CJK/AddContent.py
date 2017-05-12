# AddContent
# Created by JKChang
# 12/05/2017, 09:21
# Tag:
# Description: add a line to the certain place of the document

import os

def addContent(filePath, index, content):
    with open(filePath, 'r') as f:
        contents = f.readlines()

    contents.insert(index, content)

    with open(filePath, 'w') as f:
        contents = ''.join(contents)
        f.write(contents)


# filePath = folderPath = r'/Users/jkchang/Github/Testfolder/txt1.txt'
index = 3
t = "# Tag: \n"

folderPath = '/Users/jkchang/Github/Python/100 python/'
for path, subdirs, files in os.walk(folderPath):
    for filename in files:
        if filename.endswith(('.txt', '.py', '.java')):
            filePath = os.path.join(path, filename)
            addContent(filePath, index, t)
