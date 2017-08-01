# W3
# Created by JKChang
# 31/05/2017, 14:27
# Tag:
# Description: 

import io
import re
from datetime import datetime


def creatFile(path, name, content):
    with io.open(path + name, 'w', encoding="utf-8") as f:
        f.write(str(content))


# folderpath = r'/Users/jkchang/Github/Testfolder/'
folderpath = r'/Users/jkchang/Github/Python/w3resource/String_/'

# folderpath = r'/Users/jkchang/Github/Python/Runood_100/'
quesPath = r'/Users/jkchang/Downloads/1.txt'

questions = []
with open(quesPath) as f:
    line = f.readlines()
    for content in line:
        if content[0].isdigit():
            questions.append(content)

for q in questions:

    pat = '(\d+)\.\s+(.*)(Go to the editor)'
    res = re.match(pat, q)

    if res:
        w = True
        number = int(res.group(1))  # number
        desc = res.group(2)
        code = '-*- coding: UTF-8 -*-'
        name = 'Q' + ("%03d" % (number,))
        auther = 'JKChang'
        date = datetime.now().strftime('%a, %d/%m/%Y, %H:%M')
        tag = 'Tag: '
        des = 'Description: ' + desc

        s = "# " + code + '\n' + \
            "# " + name + '\n' + \
            "# Created by " + auther + '\n' + \
            "# " + date + '\n' + \
            "# " + tag + '\n' + \
            "# " + des + '\n'

        creatFile(folderpath,name + '.py', s)
    else:
        pass


