# Q052
# Created by JKChang
# 05/05/2017, 09:45
# Tag:  class
# Description: Define a class named Circle which can be constructed by a radius. The Circle class has a method which
#              can compute the area.

class Circle:
    def __init__(self,r):
        self.radius = r

    def area(self):
        return self.radius **2 * 3.14


aCircle = Circle(2)
print aCircle.area()