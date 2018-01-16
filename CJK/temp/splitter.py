# splitter
# Created by JKChang
# 12/01/2018, 13:13
# Tag:
# Description:

email = []
psw = []
with open('/Users/jkchang/Desktop/email.txt') as file:
    lines = file.readlines()
    for line in lines:
        res = line.strip().split('----')
        email.append(res[0])
        psw.append(res[1])

print('\n'.join(email))

