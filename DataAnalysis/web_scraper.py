# web
# Created by JKChang
# 07/03/2018, 12:28
# Tag:
# Description: 
# http://www.compjour.org/warmups/govt-text-releases/collect-lists-of-obama-press-briefings/



import requests
from os import makedirs
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from glob import glob

URL_ENDPOINT = 'https://www.whitehouse.gov/briefings-statements/page/'
MAX_PAGE_NUM = 261 #259
INDEX_PAGES_DIR = 'index-pages'

# save the lidex file to local ----------------------------------
# makedirs(INDEX_PAGES_DIR,exist_ok=True)
#
# for pagenum in range(MAX_PAGE_NUM):
#     resp = requests.get(os.path.join(URL_ENDPOINT +str(pagenum)))
#     print('Downloading',resp.url)
#
#     fname = os.path.join(INDEX_PAGES_DIR,'{}.html'.format(pagenum))
#     print('Saving',fname)
#     with open(fname,'w') as wf:
#         wf.write(resp.text)

# extract all the hyperlink -------------------------------------

# WH_BASE_URL = 'https://www.whitehouse.gov/briefings-statements/'
#
# links = []
# ip_fnames = glob(os.path.join(INDEX_PAGES_DIR, '*.html'))
# for fname in ip_fnames:
#     with open(fname, 'r') as rf:
#         txt = rf.read()
#
#     soup = BeautifulSoup(txt, 'lxml')
#     for h in soup.find_all('h2'):
#         a = h.find('a')
#         url = urljoin(WH_BASE_URL, a.attrs['href'])
#         links.append(url)
#
# with open('links.txt','w') as wf:
#     wf.write('\n'.join(links))

# extract the date and the content of the hyperlink--------------------
links =[]
links = open('links.txt','r').read().split('\n')
print(links)




