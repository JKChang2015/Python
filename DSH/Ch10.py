# Ch10
# Created by JKChang
# 09/01/2018, 13:31
# Tag:
# Description: File and Error

import os

with open('test1.txt') as f:
    contents = f.read()
    print(contents)

# ------- open file from path ----
print('---')
with open(os.path.expanduser('~/Github/Python/DSH/test1.txt')) as ff:
    contents = ff.read()
    print(contents)

# ---------read line by line -----
print('---')
with open('test1.txt') as file:
    for line in file:
        print('-' + line.rstrip())
# ------- save each line to list ----
print('---')
with open('test1.txt') as file:
    lines = file.readlines()
    res = ''
    for line in lines:
        res += line.rstrip()
        print('@' + line.rstrip())
    print('->' + res)

# ------ traverse your file -------
print('------')
with open('pi_million_digits.txt') as pi:
    contents = pi.read()

    if '0703' in contents:
        print('your B-Day is located in: ' + str(contents.find('0703') - 2) + ' of pi')
    else:
        print('Sorry, can not find your birthday')

# -------write string to the file------------
with open(os.path.expanduser('~/Github/Python/DSH/ws.txt'),'w') as f:
    f.write('Hello, python')
print('-> write done')

# -------write string to the file------------
with open(os.path.expanduser('~/Github/Python/DSH/ws.txt'),'a') as f:
    f.write('\nadd somthing to the file')
print('-> add done')