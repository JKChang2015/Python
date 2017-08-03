# -*- coding: utf-8 -*-
# CleanHTML
# Created by JKChang
# 02/06/2017, 16:03
# Tag:
# Description:

# import httplib2
# from BeautifulSoup import BeautifulSoup, SoupStrainer
#
# http = httplib2.Http()
# status, response = http.request('http://videos.yizhansou.com/210')
#
# for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
#     print link['href']


import urllib.request, urllib.error, urllib.parse
import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

html_page = urllib.request.urlopen("http://videos.yizhansou.com/210")
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    print(link.get('href').encode('utf-8'))

print('完事儿')