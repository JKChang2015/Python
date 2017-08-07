# HSP
# Created by JKChang
# 04/08/2017, 20:10
# Tag:
# Description: Travelling salesman problem
# Input: 100 postcodes
# Output: the optimized route, list?
# Strategy: 1. using google map api to extract distance information
from urllib import request
import GoogleMapsApi
import xml.etree.ElementTree as ET
import itertools

key = 'AIzaSyCODLmOUPfO51punLP1WBfoaA-FJY8UsVs'
# key = 'AIzaSyCsDP-iDmh5ulQVK6uiu0vAicaU89wQzJA'


def getdistance(ad1, ad2):
    url = r'https://maps.googleapis.com/maps/api/distancematrix/xml?units=metric&origins=%s&destinations=%s&key=%s'  %(ad1,ad2,key)

    # xml_str = request.urlopen(url).read()

    return url

stri = "CB250EN,CB99BJ,CB24,CB11EE,CB63NZ,CB23NB,CB101PZ,CB87RB,CB113SJ,CB80SH"


address = stri.split(',')
# print(address)
res = list(itertools.combinations(address,2))
# print(res)
for ad in res:
    print(ad[0] , ad[1])
    print (getdistance(ad[0],ad[1]))