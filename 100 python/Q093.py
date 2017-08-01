# Q093
# Created by JKChang
# 09/05/2017, 15:37
# Tag: class and inherent
# Description: Define a class Person and its two child classes: Male and Female. All classes have a method "getGender"
#              which can print "Male" for Male class and "Female" for Female class.

class Person(object):
    def getGender(self):
        return 'Unknown'

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return 'Female'


aMale = Male()
aFemale= Female()
print(aMale.getGender())
print(aFemale.getGender())