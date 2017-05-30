# -*- coding: utf-8 -*-
# Q100
# Created by JKChang
# Tag: term Counter
# 09/05/2017, 15:37
# Description: term counter,remove punctuation

# from collections import Counter
# sentence = "Hello there this is a test.a Hello there this this was a test, but now it is not."
# words = sentence.split(' ')
# counts = Counter(words)
# print counts


import operator
import string


class Counter():
    def __init__(self):
        self.dict = {}

    def add(self, item):
        self.dict[item] = self.dict.get(item, 0) + 1

    def counts(self):
        # sort dictionary according to the values
        result = sorted(self.dict.items(), key=operator.itemgetter(1), reverse=True)
        return result


c = Counter()
s = "Hello there this is a test. hello there this was a test, but now it is not."
replace_punctuation = string.maketrans(string.punctuation, ' ' * len(string.punctuation))
text = s.lower().translate(replace_punctuation)
words = text.split()

for i in words:
    c.add(i)
res = c.counts()

for i in res:
    print '%s: %s' % (i[0], i[1])