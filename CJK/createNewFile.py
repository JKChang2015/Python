# createNewFile
# Created by JKChang
# 12/05/2017, 10:48
# Tag:
# Description: create new file with temples

import io
from datetime import datetime
import string

serial = []


def creatFile(path, name, content):
    with io.open(path + name, 'w', encoding="utf-8") as f:
        f.write(str(content))

def extractQuestion(Filepath):
    with open(Filepath) as f:

        content = f.read()
        s = content
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

questionPath = '/Users/jkchang/Downloads/ree.txt'
questions = extractQuestion(questionPath)

targetPath = r'/Users/jkchang/Github/Python/w3resource/rex/'
# print "%03d" % (87,)
# path = r'/Users/jkchang/Github/Testfolder/'
# path = r'/Users/jkchang/Github/Python/Runood_100/'

total = len(serial)

for i in range(1,total+1):
    code = '-*- coding: UTF-8 -*-'
    name = 'Q' + ("%03d" % (i,))
    auther = 'JKChang'
    date = datetime.now().strftime('%a, %d/%m/%Y, %H:%M')
    tag = 'Tag: '
    des = 'Description: ' + questions[i-1]

    s = "# " + code + '\n' + \
        "# " + name + '\n' + \
        "# Created by " + auther + '\n' + \
        "# " + date + '\n' + \
        "# " + tag + '\n' + \
        "# " + des + '\n'

    creatFile(targetPath, name + '.py', s)
