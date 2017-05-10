# -*- coding: utf-8 -*-
# Q0100
# Created by JKChang
# 09/05/2017, 15:37
# Description: term frequency counter

class Counter(object):
    def __init__(self):
        self.dict = {}

    def add(self, item):
        dict[item] = dict.get(item, 0) + 1  # 返回指定键的值，如果值不在字典中返回default值

    def counts(self, desc=None):
        result = [[val, key] for (key, val) in self.dict.items()]
        result.sort()
        if desc:
            result.reverse()
        return result

if __name__ == '__main__':
    sentence = "Hello there this is a test.  Hello there this was a test, but now it is not."
    words = sentence.split(' ')
    print words