# createNewFile
# Created by JKChang
# 12/05/2017, 10:48
# Tag:
# Description: create new file with temples

import io
from datetime import datetime


def creatFile(path, name, content):
    with io.open(path + name, 'w', encoding="utf-8") as f:
        f.write(unicode(content))


# print "%03d" % (87,)

# path = r'/Users/jkchang/Github/Testfolder/'
path = r'/Users/jkchang/Github/Python/Runood_100/'

for i in range(14, 101):
    code = '-*- coding: UTF-8 -*-'
    name = 'R' + ("%03d" % (i,))
    auther = 'JKChang'
    date = datetime.now().strftime('%a, %d/%m/%Y, %H:%M')
    tag = 'Tag: '
    des = 'Description: '

    s = "# " + code + '\n' + \
        "# " + name + '\n' + \
        "# Created by " + auther + '\n' + \
        "# " + date + '\n' + \
        "# " + tag + '\n' + \
        "# " + des + '\n'

    # creatFile(path, name + '.py', s)
