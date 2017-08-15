# -*- coding: utf-8 -*-

# CleanHTML
# Created by JKChang
# 02/06/2017, 16:03
# Tag:
# Description:


import urllib.request
import urllib.parse
import requests

url = 'http://videos.yizhansou.com/422'
from bs4 import BeautifulSoup

html =urllib.request.urlopen(url)
# web = urllib.request.Request(html)
content = html.read().decode('gbk').encode('utf8')


# print(content.encode('latin-1').decode('gbk').encode('utf-8'))
# print(type(content))
# print(content)







# # coding:utf-8
# import re
# import requests
#
# # 获取网页内容
# r = requests.get('http://videos.yizhansou.com/210')
# data = r.text
#
#
# # 利用正则查找所有连接
# link_list =re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')" ,data)
# for url in link_list:
#     # print (url.encode('UTF8').decode('unicode_escape'))
#     print(url)

# import httplib2
# from BeautifulSoup import BeautifulSoup, SoupStrainer
#
# http = httplib2.Http()
# status, response = http.request('http://videos.yizhansou.com/210')
#
# for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
#     print link['href']

# import urllib.request
# from bs4 import BeautifulSoup
#
# import urllib3
# import re
#
# u = 'http://videos.yizhansou.com/210'
# html_page = urllib.request.urlopen(u)
# soup = BeautifulSoup(html_page)
# for link in soup.findAll('a'):
#     print (link.get('href'))


# import urllib.request
# import urllib.error
# import urllib.parse
#
# from bs4 import BeautifulSoup
#
# url = 'http://videos.yizhansou.com/210'
#
# request = urllib.request.Request(url)
# response = urllib.request.urlopen(request)
# content = response.read()
# soup = BeautifulSoup(content,'html')
# for link in soup.findAll('a'):
#     h = link.get('href')
#     print(h)
#     print(h.decode('utf-8'))
#     # print(type(link.get('href')))
