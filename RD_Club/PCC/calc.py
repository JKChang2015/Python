# testCase
# Created by JKChang
# 10/01/2018, 11:02
# Tag:
# Description: unittest case

def add(x, y):
    '''Add Function'''
    return x + y


def substract(x, y):
    '''Substract Function'''
    return x - y


def multiply(x, y):
    '''Multiply Function'''
    return x * y


def devide(x, y):
    'Divide Function'
    if y == 0:
        raise ValueError('Can not divide by zero')
    return x / y
