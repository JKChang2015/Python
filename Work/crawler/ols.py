# ontology_com
# Created by JKChang
# 11/06/2018, 12:46
# Tag:
# Description: extract list of ontologies from the OLS

import csv

import requests
from bs4 import BeautifulSoup


class Ontology(object):
    def __init__(self, name, fullname, url, description):
        self.name = name
        self.fullname = fullname
        self.url = url
        self.description = description


url = 'https://www.ebi.ac.uk/ols/ontologies'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

ontos = soup.findAll('tbody')[0].findAll('tr')

res = []

for onto in ontos:
    # full name
    try:
        name = onto.findAll('a')[0].text.strip()
    except:
        name = onto.findAll('span')[0].text.strip()

    # url
    try:
        url = onto.findAll('a')[0].attrs['href'].strip()
    except:
        url = ''

    # abbreviation
    abb = onto.findAll('span', {"class": "ontology-source"})[0].text.strip()

    # description
    des = onto.findAll('td')[2].text.strip()

    a = Ontology(name=abb, fullname=name, url=url, description=des)
    res.append(a)

res = sorted(res, key=lambda onto: onto.name)

# save ontology
spamWriter = csv.writer(open('ols ontology list.csv', 'w'))
spamWriter.writerow(['abbr',  'name',  'url', 'description'])

for r in res:
    out = [r.name, r.fullname, r.url, r.description]
    spamWriter = csv.writer(open('ols ontology list.csv', 'a'))
    spamWriter.writerow(out)

# meta = []
# with open('./Desktop/ols.csv')as f:
#     lines = f.readlines()
#     for line in lines:
#         meta.append(line.strip())
#
# ols = []
# for onto in res:
#     ols.append(onto.name)
#
#
# def intersection(lst1, lst2):
#     return list(set(lst1) & set(lst2))
#
#
# print(sorted(intersection(ols, meta)))
