# CleanHTML
# Created by JKChang
# 02/06/2017, 16:03
# Tag:
# Description:

import io

from bs4 import BeautifulSoup

htmlPath = '/Users/jkchang/Downloads/t3.html'
soup = BeautifulSoup(open(htmlPath))
print soup.prettify()
# with io.open(htmlPath) as f:
#     text = f.read()
#     tree = BeautifulSoup(text)
#     good = tree.prettify()
#     print good
