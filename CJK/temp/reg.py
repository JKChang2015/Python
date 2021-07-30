# -*- coding: utf-8 -*-
# reg
# Created by JKChang
# 09/05/2017, 10:09
# Description: regular expression

import re

str1 = 'information retrieval tutorial'

pa = re.compile(r'information', re.IGNORECASE)  # 原字符串 'r', 忽略大小写 re.I


ma = pa.match(str1)
print(ma.group())  # matching result
print(ma.span())  # matching index

print(ma.string)  # The documents
print(ma.re)  # object of the target pattern
