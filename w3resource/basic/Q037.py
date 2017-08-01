# -*- coding: UTF-8 -*-
# Q037
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: print
# Description: Write a Python program to display your details like name, age, address in three different lines. 

class Person(object):
    def __init__(self,name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def printInfo(self):
        print('name = %s\nage = %s\naddress = %s' %(self.name, self.age, self.address))


david = Person('David','12','longfellow')
david.printInfo()