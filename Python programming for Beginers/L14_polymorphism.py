# L14_polymorphism
# Created by JKChang
# 22/02/2017, 14:10
# Description: a polymorphism example

class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = self.width * self.height / 2.0
        return area


class Square:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        area = float(self.width * self.height)
        return area


tra = Triangle(6, 6)
print(tra.getArea())
sqr = Square(6, 6)
print(sqr.getArea())
