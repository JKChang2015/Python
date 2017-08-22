# -*- coding: UTF-8 -*-
# Q015
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: format print
# Description: Write a Python function to create the HTML string with tags around the word(s). 

def func(word, tag):
    print('<%s> %s </%s>' % (tag, word, tag))


func('information retrieval', 'title')
