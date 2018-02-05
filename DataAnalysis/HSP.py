# HSP
# Created by JKChang
# 04/08/2017, 20:10
# Tag:
# Description: Travelling salesman problem
# Input: 100 postcodes
# Output: the optimized route, list?

import googlemaps
from googlemaps.distance_matrix import distance_matrix
import itertools
from dicttoxml import dicttoxml
import xml.etree.ElementTree as ET
import lxml.etree as etree


def XMLPretty(string):
    root = etree.fromstring(string)
    return etree.tostring(root, pretty_print=True)


def getdistance(original, destination):
    client = googlemaps.Client(key='AIzaSyCsDP-iDmh5ulQVK6uiu0vAicaU89wQzJA')
    matrix = client.distance_matrix(original, destination)
    xml_str = dicttoxml(matrix, attr_type=False)
    # print(XMLPretty(xml_str).decode('utf8'))
    root = ET.fromstring(xml_str)
    for distance in root.iter('distance'):
        m = distance.find('value').text
        return m


stri = "CB250EN,CB99BJ,CB24,CB11EE,CB63NZ,CB23NB,CB101PZ,CB87RB,CB113SJ,CB80SH"
address = stri.split(',')
# print(address)
address_pairs = list(itertools.combinations(address, 2))
# print(res)
for address in address_pairs:
    print(address[0], address[1], getdistance(address[0], address[1]))

