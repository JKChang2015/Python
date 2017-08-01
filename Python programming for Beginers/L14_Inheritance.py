# L14_Inheritance
# Created by JKChang
# 22/02/2017, 14:41
# Description: inherit example

class Parent:
    __parentAttr = 100

    def __init__(self):
        print("parent's construction method")

    def prentMethod(self):
        print("parent's method")

    def getAttr(self):
        print("parent's attribute: ", self.parentAttr)

    def setAttr(self, attr):
        self.parentAttr = attr


class Child(Parent):
    def __init__(self):
        print("Child's construction method")

    def childMethod(self):
        print("Child's method")


c = Child()
c.childMethod()
c.prentMethod()
c.setAttr(200)
c.getAttr()
