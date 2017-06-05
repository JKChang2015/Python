# -*- coding: UTF-8 -*-
# Q007
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: double negation
# Description: Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given
#              string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the
#              resulting string.
#
# Sample String : 'The lyrics is not that poor!'
# Expected Result : 'The lyrics is good!'

def not_poor(str1):
    snot = str1.lower().find('not')  # location
    sbad = str1.lower().find('poor')  # location

    if sbad > snot:
        str1 = str1.replace(str1[snot:(sbad + 4)], 'good')  # replace(target,replacement)

    return str1


print not_poor('The lyrics is not that poor!')
