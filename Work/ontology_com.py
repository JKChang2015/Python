# ontology_com
# Created by JKChang
# 11/06/2018, 12:46
# Tag:
# Description: extract list of ontologies from the OLS

class ontology(object):
    def __init__(self, name, fullname, url, description):
        self.name = name
        self.fullname = fullname
        self.url = url
        self.description = description


import re
import urllib.error
import urllib.parse
import urllib.request

import requests
from bs4 import BeautifulSoup
from stripogram import html2text

url = 'https://bioportal.bioontology.org/ontologies'

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}

req = urllib2.Request(url, headers=hdr)

try:
    page = urllib2.urlopen(req)
except e:
    print(e.fp.read())

print(type(page))


