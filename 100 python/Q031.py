# Q31
# Created by JKChang
# 28/04/2017, 13:48
# Tag: length of string
# Description: Define a function that can accept two strings as input and print the string with maximum length in
#              console. If two strings have the same length, then the function should print all strings line by line.

def PrintValue(s1, s2):
    if(len(s1) > len(s2)):
        print(s1)
    elif (len(s1) < len(s2)):
        print(s2)
    else:
        print(s1)
        print(s2)

PrintValue('hello', 'world')