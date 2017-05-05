# Q053
# Created by JKChang
# 05/05/2017, 09:45
# Description: Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has
#              a method which can compute the area.

class Rectangle:

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


aRectangle = Rectangle(2,4)
print aRectangle.area()