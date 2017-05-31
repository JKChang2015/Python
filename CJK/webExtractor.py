# webExtractor
# Created by JKChang
# 30/05/2017, 21:39
# Tag:
# Description:
import urllib2

url = 'http://www.w3resource.com/python-exercises/python-basic-exercises.php'

response = urllib2.urlopen(url)
html = response.read()
print html


# file = urllib.urlopen('http://helloworldbook.com/data/message.txt')
# message = file.read()
# print message