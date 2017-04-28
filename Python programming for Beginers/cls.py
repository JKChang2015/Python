# cls
# Created by JKChang
# 28/04/2017, 12:26
# Description: learning the Python classes

class employee:

    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        employee.empCount += 1

    def displayCount(self):
        print 'Total employee %d' %employee.empCount

    def displayEmployee(self):
        print 'Name: %s \nSalary: %s' % (self.name, self.salary)


dav = employee('David', 100)
dav.displayCount()
dav.displayEmployee()



