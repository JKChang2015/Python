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
with open(os.path.expanduser('~/Github/Python/RD_Club/PPC/test1.txt')) as ff:
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
print('---')
with open('pi_million_digits.txt') as pi:
    contents = pi.read()

    if '0703' in contents:
        print('your B-Day is located in: ' + str(contents.find('0703') - 2) + ' of pi')
    else:
        print('Sorry, can not find your birthday')

# -------write string to the file------------
print('---')
with open(os.path.expanduser('~/Github/Python/RD_Club/PPC/ws.txt'), 'w') as f:
    f.write('Hello, python')
print('-> wrote done')

# -------write string to the file------------
print('---')
with open(os.path.expanduser('~/Github/Python/RD_Club/PPC/ws.txt'), 'a') as f:
    f.write('\nadd somthing to the file')
print('-> add done')

# ———————————save the data to the file———————
print('---')
import json

num = [2, 3, 5, 7, 21]
fileName = os.path.expanduser('~/Github/Python/RD_Club/PPC/numbers.json')
with open(fileName, 'w') as f_obj:
    json.dump(num, f_obj)
print('-> Data saved...')

# ———————————load the data from the file———————
print('---')

fileName = os.path.expanduser('~/Github/Python/RD_Club/PPC/numbers.json')
with open(fileName) as f:
    nums = json.load(f)

print(nums)
print(type(nums))
print('-> Data loaded...')
# -----------Json example -------------------
# save the data to the file
print('---')

userName = input('Pls input your name: ')
fileName = os.path.expanduser('~/Github/Python/RD_Club/PPC/user_name.json')
with open(fileName, 'w') as f:
    json.dump(userName, f)
    print('-> Name saved')

print('When you come back..............')
with open(fileName) as nameFile:
    name = json.load(nameFile)
    print('\nHello', name, 'welcome back...')

# json with Python: http://developer.rhino3d.com/guides/rhinopython/python-xml-json/

# -----------reconstruction-------------
print('---')


