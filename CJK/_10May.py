# _10May
# Created by JKChang
# 10/05/2017, 19:59
# Description:

rmPath = '/Users/jkchang/Github/Python/100 python/README.md'
folderPath = '/Users/jkchang/Github/Python/100 python/'

# print '\n'.join(os.listdir(folderPath))

file = open(folderPath + 'Q080.py')
for line in file:
    if line.startswith("# Creat"):
        print line
