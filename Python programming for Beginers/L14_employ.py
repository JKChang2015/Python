# -*- coding: UTF-8 -*-
# L14_employ
# Created by JKChang
# 21/02/2017, 10:33
# Description: 

# -*- coding: UTF-8 -*-


class Employee:
    'some thing here'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def __del__(self):
        name = self.name
        print 'destroty', name

    def dispalyCount(self):
        print 'total Employee %d' % Employee.empCount

    def displayEmployee (self):
        print 'Name:', self.name, '  ,Salary:', self.salary


empl1 = Employee('Zara', 2000)
empl2 = Employee('David', 4090)
empl1.displayEmployee()
empl2.displayEmployee()

print 'total num of employee is %d' % Employee.empCount

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

del empl1
del empl2
