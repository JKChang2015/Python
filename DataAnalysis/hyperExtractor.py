# ttt
# Created by JKChang
# 08/08/2017, 12:26
# Tag:
# Description: 

import re
import urllib.request

url = 'http://videos.yizhansou.com/3884'
fp = urllib.request.urlopen(url)
mybytes = fp.read()

mystr = mybytes.decode('gbk').strip()
fp.close()

links = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", mystr)

for link in links:
    if link.__contains__('ed2k'):
        print(link)