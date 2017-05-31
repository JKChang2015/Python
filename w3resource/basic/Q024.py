# -*- coding: UTF-8 -*-
# Q024
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: identify char in string
# Description: Write a Python program to test whether a passed letter is a vowel or not. 

def is_vowel(char):
    return char.lower() in 'aeiou'


print is_vowel('c')
print is_vowel('E')
