# Q056
# Created by JKChang
# 05/05/2017, 09:45
# Tag: exception
# Description: Write a function to compute 5/0 and use try/except to catch the exceptions.

def throws():
    return 5 / 0


try:
    throws()
except ZeroDivisionError:
    print 'division by 0'
except Exception, err:
    print 'something wrong'
finally:
    print 'done'
