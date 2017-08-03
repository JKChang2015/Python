# etreeTest
# Created by JKChang
# 01/08/2017, 15:19
# Tag:
# Description: 

from lxml import etree

root = etree.Element("root", interested = "totally")
# print(etree.tostring(root).decode('utf-8'))
root.append(etree.Element("ch1"))
ch2 = etree.SubElement(root, "ch2")
ch2.text = "This is ch2's content"
ch3 = etree.SubElement(root, "ch3")
print(etree.tostring(root, pretty_print=True).decode('utf-8'))

print(len(root))
