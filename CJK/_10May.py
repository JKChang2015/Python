# _10May
# Created by JKChang
# 10/05/2017, 19:59
# Description:

import os


def mappingFormat(path):
    if filepath.endswith('.txt'):
        return 'Text'
    elif filepath.endswith('.py'):
        return 'Python'
    elif filepath.endwith('.java'):
        return'Java'
    else:
        pass

# number # [name](link) # flag #language

# rmPath = '/Users/jkchang/Github/Python/100 python/README.md'
folderPath = '/Users/jkchang/Github/Python/100 python/'
# folderPath = r'/Users/jkchang/Github/Testfolder/'

pathList = []
format = ''

for path, subdirs, files in os.walk(folderPath):
    for filename in files:
        f = os.path.join(path, filename)
        if f.endswith(('.txt', '.py', '.java')):
            pathList.append(f[len(folderPath) - 1:])

# print '\n'.join(pathList)
for filepath in pathList:
    format = mappingFormat(filepath)
    print 'this file is ', format
    f = open(folderPath + filepath)
    print f.read()





# f = open(os.getcwd+ pathList[0])
# print f.read



# s = os.walk(folderPath)
# li = [x[0] for x in s]
# print '\n'.join(li)



# for roots, dirs, filenames in s:  # String, List, list
#     print roots
#     print len(dirs)
#     print dirs
#     s = filenames
#     print type(s)

# print dirs
# print type(roots)
# print type(dirs)
# print type(files)
# break




# l = os.path.split(rmPath)
# print l[0]
# print l[1]
#
# # ll = os.path.splitext(rmPath)
# # print ll[0]
# # print ll[1]
# #
# print os.path.basename(rmPath)



# print '\n'.join(os.listdir(folderPath))

# file = open(folderPath + 'Q080.py')
# for line in file:
#     if line.startswith("# Creat"):
#         print line
