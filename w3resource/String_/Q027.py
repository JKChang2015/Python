# -*- coding: UTF-8 -*-
# Q027
# Created by JKChang
# Thu, 01/06/2017, 16:31
# Tag: remove indentation(dedent)
# Description: Write a Python program to remove existing indentation from all of the lines in a given text.

import textwrap

sample_text = '''
    \tPython is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''

print(textwrap.dedent(sample_text))