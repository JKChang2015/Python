# web
# Created by JKChang
# 07/03/2018, 12:28
# Tag:
# Description: 
# http://www.compjour.org/warmups/govt-text-releases/collect-lists-of-obama-press-briefings/

import requests
from os import makedirs
import os

URL_ENDPOINT = 'https://www.whitehouse.gov/briefings-statements/page/'
MAX_PAGE_NUM = 261 #259
INDEX_PAGES_DIR = 'index-pages'

makedirs(INDEX_PAGES_DIR,exist_ok=True)

for pagenum in range(MAX_PAGE_NUM):
    resp = requests.get(os.path.join(URL_ENDPOINT +str(pagenum)))
    print('Downloading',resp.url)

    fname = os.path.join(INDEX_PAGES_DIR,'{}.html'.format(pagenum))
    print('Saving',fname)
    with open(fname,'w') as wf:
        wf.write(resp.text)
