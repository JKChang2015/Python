import time
from urllib.request import urlopen

from bs4 import BeautifulSoup

stockItem = '000660'
url = 'http://finance.naver.com/item/sise_day.nhn?code=' + stockItem
html = urlopen(url)
source = BeautifulSoup(html.read(), "html.parser")
maxPage = source.find_all("table", align="center")
mp = maxPage[0].find_all("td", class_="pgRR")
mpNum = int(mp[0].a.get('href')[-3:])

for page in range(1, mpNum + 1):
    print(str(page))
    url = 'http://finance.naver.com/item/sise_day.nhn?code=' + stockItem + '&page=' + str(page)
    html = urlopen(url)
    source = BeautifulSoup(html.read(), "html.parser")
    srlists = source.find_all("tr")
    isCheckNone = None

    if ((page % 1) == 0):
        time.sleep(1.50)
    for i in range(1, len(srlists) - 1):
        if (srlists[i].span != isCheckNone):
            srlists[i].td.text
            res = srlists[i].find_all("td", align="center")[0].text, srlists[i].find_all("td", class_="num")[0].text
            output = '\t'.join(res)
            # print(output)
            with open("hzz 000660.tsv", "a") as myfile:
                myfile.write(output + '\n')
