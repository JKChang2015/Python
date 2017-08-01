# Q81
# Created by JKChang
# 09/05/2017, 15:37
# Tag: compress and decompress
# Description: Please write a program to compress and decompress the string "hello world!hello world!hello
#              world!hello world!".

import zlib

s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))
