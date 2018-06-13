# ontology_com
# Created by JKChang
# 11/06/2018, 12:46
# Tag:
# Description: extract list of ontologies from the OLS

import requests
from bs4 import BeautifulSoup

url = 'https://www.ebi.ac.uk/ols/ontologies'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

tbody = soup.findAll('tbody')
ontos = tbody[0].findAll('tr')


class Ontology(object):
    def __init__(self, name, fullname, url, description):
        self.name = name
        self.fullname = fullname
        self.url = url
        self.description = description


res = []

for onto in ontos:
    # full name
    try:
        name = onto.findAll('a')[0].text
    except:
        name = onto.findAll('span')[0].text

    # abbreviation
    abb = onto.findAll('span', {"class": "ontology-source"})[0].text

    # url
    path = 'https://www.ebi.ac.uk/'
    try:
        url = onto.findAll('a')[0].attrs['href']
    except:
        url = ''

    # description
    des = onto.findAll('td')[2].text

    a = Ontology(name=abb, fullname=name, url=url, description=des)
    res.append(a)

meta = []
with open('./Desktop/ols.csv')as f:
    lines = f.readlines()
    for line in lines:
        meta.append(line.strip())

ols = []
for onto in res:
    ols.append(onto.name)


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


print(sorted(intersection(ols, meta)))
