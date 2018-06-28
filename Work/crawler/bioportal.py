# bioportal
# Created by JKChang
# 12/06/2018, 10:03
# Tag:
# Description: extract list of ontology from 'https://bioportal.bioontology.org/ontologies'

import csv
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class bio_ontology(object):
    name, abbr, url, description, date = '', '', '', '', ''
    cls_num, pro_num = '', ''

    def __init__(self, abbr, name, url):
        self.name = name
        self.abbr = abbr
        self.url = url


# save ontologies
def load_onto(onto):
    # name & abbr
    title = onto.findAll('a', {'class': 'ng-binding'})[0].text.strip()
    name = re.findall('[^()]+', title)[0]
    abbrs = re.findall('[^()]+', title)[1]

    # url
    path = 'https://bioportal.bioontology.org'
    url = path + onto.findAll('a')[0].attrs['href']
    ontology = bio_ontology(abbr=abbrs, name=name, url=url)

    try:
        # cls_number
        cls_num = onto.findAll('div', {'class': "badge_count ng-binding"})[0].text.strip()
        cls_num = cls_num.replace(',', '')
        ontology.cls_num = cls_num
    except:
        pass

    try:
        # pro_number
        pro_num = onto.findAll('div', {'class': "badge_count ng-binding"})[1].text.strip()
        pro_num = pro_num.replace(',', '')
        ontology.pro_num = pro_num
    except:
        pass

    try:
        # description
        des = onto.findAll('p', {'class': "ng-binding"})[0].text.strip()
        ontology.description = des.replace('\n', '')
    except:
        pass

    try:
        # date
        upload = onto.findAll('span', {'class': 'ont-info ng-binding'})[0].text.strip()
        date = upload.split(':', 1)[1].strip()
        ontology.date = date
    except:
        pass

    return ontology


# simulation browser
url = 'https://bioportal.bioontology.org/ontologies'
driver = webdriver.Chrome()
driver.get(url)

# driver.find_element_by_id("include_ontology_view").click()
wait = WebDriverWait(driver, 10)
soup = BeautifulSoup(driver.page_source, "html.parser")

# all ontologies
ontologies = soup.findAll('div', {'class': "ontology grid-parent clearfix ng-scope"})

res = []
for onto in ontologies:
    data = load_onto(onto)
    if data.cls_num != '':
        res.append(data)

res = sorted(res, key=lambda onto: onto.abbr)

# save ontology
spamWriter = csv.writer(open('./crawler/bioportal ontology list.csv', 'w'))
spamWriter.writerow([
    'name', 'abbr', 'class_num', 'pro_num', 'modified date', 'url',
    'description'
])
for r in res:
    out = [r.name, r.abbr, r.cls_num, r.pro_num, r.date, r.url, r.description]
    spamWriter = csv.writer(open('./crawler/bioportal ontology list.csv', 'a'))
    spamWriter.writerow(out)
