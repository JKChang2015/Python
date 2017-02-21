# -*- coding: UTF-8 -*-
# L14_employ
# Created by JKChang
# 21/02/2017, 10:33
# Description: 

# -*- coding: UTF-8 -*-


class Employee:
    '所有员工类型'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def dispalyCount(self):
        print 'total Employee %d' % Employee.empCount

    def displayEmployee (self):
        print 'Name:', self.name, '  ,Salary:', self.salary