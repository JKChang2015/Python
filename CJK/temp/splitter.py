# splitter
# Created by JKChang
# 12/01/2018, 13:13
# Tag:
# Description:

# email = []
# psw = []
# with open('/Users/jkchang/Desktop/email.txt') as file:
#     lines = file.readlines()
#     for line in lines:
#         res = line.strip().split('----')
#         email.append(res[0])
#         psw.append(res[1])
#
# print('\n'.join(email))


code = []
psw = []
s = 0
linecount = 0
with open('/Users/jkchang/Desktop/code.txt') as file:
    lines = file.readlines()
    for line in lines:
        linecount += 1
        res = line.strip().split(' ')
        code.append(res[0] + res[1])
        psw.append(res[2])
        s += int(res[0])
        if (linecount % 10 == 0):
            code.append(' ')
            psw.append(' ')

print('\n'.join(code))
print('\n'.join(psw))
print(s)
