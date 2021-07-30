# createNewFile
# Created by JKChang
# 12/05/2017, 10:48
# Tag:
# Description: create new python file with temples

import io
import string
from datetime import datetime

serial = []


def creatFile(path, name, content):
    with io.open(path + name, 'w', encoding="utf-8") as f:
        f.write(str(content))


def extractQuestion(Filepath):
    with open(Filepath) as f:

        content = f.read()
        s = content
        s = s.replace('Go to the editor', '')
        s = s.replace('Click me to see the sample solution', '')
        lines = content.split('\n')

        for line in lines:
            translator = str.maketrans('', '', string.punctuation)
            line = line.translate(translator)
            if len(line) != 0 and line != '\n':
                value = line.split()[0]
                if value.isdigit():
                    serial.append(value)
        print(serial)

        res = []
        for ser in serial[1:]:
            res.append(s.split(ser, 1)[0])
            s = ser + s.split(ser, 1)[1]

        res.append(s)
        print('>'.join(res))
        return res


questionPath = r'/Users/jkchang/Downloads/ree.txt'
questions = extractQuestion(questionPath)

# targetPath = r'/Users/jkchang/Github/Testfolder/'
targetPath = r'/Users/jkchang/Github/Python/w3resource/List_/'
# print "%03d" % (87,)
# path = r'/Users/jkchang/Github/Testfolder/'
# path = r'/Users/jkchang/Github/Python/Runood_100/'

total = len(serial)

for i in range(1, total + 1):
    code = '-*- coding: UTF-8 -*-'
    name = 'Q' + ("%03d" % (i,))
    auther = 'JKChang'
    date = datetime.now().strftime('%a, %d/%m/%Y, %H:%M')
    tag = 'Tag: '
    des = 'Description: ' + questions[i - 1]

    s = "# " + code + '\n' + \
        "# " + name + '\n' + \
        "# Created by " + auther + '\n' + \
        "# " + date + '\n' + \
        "# " + tag + '\n' + \
        "# " + des + '\n'

    creatFile(targetPath, name + '.py', s)
