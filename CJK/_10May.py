# _10May
# Created by JKChang
# 10/05/2017, 19:59
# Description:


def mappingFormat(path):
    if filepath.endswith('.txt'):
        return 'Text'
    elif filepath.endswith('.py'):
        return 'Python'
    elif filepath.endwith('.java'):
        return 'Java'
    else:
        pass


def wMarkovTable(number, name, link, language, tag):
    return '|' + number + '|' + \
           '[' + name + ']' + \
           '(' + link + ')|' + \
           tag + '|' + \
           language + '|'


def wMarkovTableHead(listofHead):
    res = ['', '']
    for x in listofHead:
        if x != 'link':
            res[0] += (x + '|')
            res[1] += ('--' + '|')
    return '|' + res[0] + '\n' + '|' + res[1]


li = ('#', 'title', 'language', 'tag')
print wMarkovTableHead(li)
print wMarkovTable('01', 'Q001', '/Users/jkchang/Github/Python/100 python/', 'range', 'Python')

#
# # number # [name](link) # tag #language
#
# # rmPath = '/Users/jkchang/Github/Python/100 python/README.md'
# folderPath = '/Users/jkchang/Github/Python/100 python/'
# # folderPath = r'/Users/jkchang/Github/Testfolder/'
#
# pathList = []
# format = ''
#
# for path, subdirs, files in os.walk(folderPath):
#     for filename in files:
#         f = os.path.join(path, filename)
#         if f.endswith(('.txt', '.py', '.java')):
#             pathList.append(f[len(folderPath) - 1:])
#
# # print '\n'.join(pathList)
# for filepath in pathList:
#     format = mappingFormat(filepath)
#     print 'this file is ', format
#     f = open(folderPath + filepath)
#     print f.read()
