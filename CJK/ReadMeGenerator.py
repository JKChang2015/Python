# ReadMeGenerator
# Created by JKChang
# 10/05/2017, 19:59
# Description:

import io
import os


def mappingFormat(filepath):
    if filepath.endswith('.txt'):
        return 'Text'
    elif filepath.endswith('.py'):
        return 'Python'
    elif filepath.endwith('.java'):
        return 'Java'
    else:
        pass


def wMarkovTable(number, name, link, language, tag):
    return '|' + number + \
           '|[' + name + ']' + '(' + link + ')|' + \
           language + '|' + tag + '|'


def wMarkovTableHead(listofHead):
    res = ['', '']
    for x in listofHead:
        if x != 'link':
            res[0] += (x + '|')
            res[1] += ('--' + '|')
    return '|' + res[0] + '\n' + '|' + res[1]


# folderPath = r'/Users/jkchang/Github/Testfolder/'

# folderPath = '/Users/jkchang/Github/Python/Runood_100/'
folderPath = '/Users/jkchang/Github/Python/100 Python/'
rmPath = folderPath + '/README.md'
title = ['#', 'Title', 'Language', 'Description']

# ----------- For each file----------------------
pathList = []
body = []
number = 0

for path, subdirs, files in os.walk(folderPath):
    for filename in files:
        if filename.endswith(('.txt', '.py', '.java')):
            number += 1
            name = os.path.splitext(filename)[0]
            filePath = os.path.join(path, filename)
            link = '.' + filePath[len(folderPath) - 1:]
            language = mappingFormat(filename)

            # -- tag --
            tag = ''
            with open(filePath) as f:
                line = f.readlines()
                for content in line:
                    if 'Tag' in content:
                        tag = content[content.index(':') + 1:].strip().capitalize()

            body.append(wMarkovTable(str(number), name, link, language, tag))

# ----------- For each file----------------------


header = wMarkovTableHead(title)
body = '\n'.join(body)
print header + '\n' + body

# with io.open(rmPath, 'w', encoding="utf-8") as f:
#      f.write(unicode(header + '\n' + body))
