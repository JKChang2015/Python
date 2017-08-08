# webExtractor
# Created by JKChang
# 30/05/2017, 21:39
# Tag:web extractor
# Description:
import urllib.request, urllib.error, urllib.parse
import requests
from bs4 import BeautifulSoup
from stripogram import html2text
import re


url = 'http://www.w3resource.com/python-exercises/python-basic-exercises.php'
html = requests.get(url).text
text = html2text(html)
l = text.encode('utf-8').split('\n')
index = 1

pat = '(/d+)/. '
for line in l:
    # if len(line) ==0:
    #     continue
    # elif line[0].isdigit():
        print(line)


    # if line[0].isdigit():
#        print line.encode('utf-8')


# print html.encode('utf-8')
#
# soup = BeautifulSoup(html,'lxml')
# res = soup.findAll("article", {"class": "listingItem"})
# print type(res)
# for r in res:
#     print("Company Name: " + r.find('a').text)
#     print("Address: " + r.find("div", {'class': 'address'}).text)
#     print("Website: " + r.find_all("div", {'class': 'pageMeta-item'})[3].text)

# hdr = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#     'Accept-Encoding': 'none',
#     'Accept-Language': 'en-US,en;q=0.8',
#     'Connection': 'keep-alive'}
#
# req = urllib2.Request(url, headers=hdr)
#
# try:
#     page = urllib2.urlopen(req)
# except urllib2.HTTPError, e:
#     print e.fp.read()
#
# content = page.read()
# print content
