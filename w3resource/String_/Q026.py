# -*- coding: UTF-8 -*-
# Q026
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: fix width output
# Description: Write a Python program to display formatted text (width=50) as output. 

import textwrap

s = """Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java."""

print(textwrap.fill(s, width=50))  # break_long_words=False, replace_whitespace=False
