# multiplication_table
# Created by JKChang
# 18/11/2019, 13:07
# Tag:
# Description: 

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j} x {i} = ' + str(i * j), end='\t')
#     print()
#
#
#
# print('\n'.join('\t'.join([f'{j} x {i} = ' + str(j * i) for j in range(1, i + 1)]) for i in range(1, 10)))

# # Method 1
# def devPrime(num, res):
#     for i in range(2, num + 1):
#         if num % i == 0:
#             res.append(i)
#             return devPrime(num // i, res)
#
#
# res = []
# devPrime(124, res)
# print(res)
#
#
# # Method 2
# def devPrime2(num):
#     res = []
#     while num > 2:
#         for i in range(2, num + 1):
#             if num % i == 0:
#                 res.append(i)
#                 num = num // i
#                 break
#     return res
#
#
# r = devPrime2(124)
# print(r)

#
# def findMax(l):
#     max = l[0]
#     for num in l:
#         if num > max:
#             max = num
#
#     return max
#
#
# def findLongest(s):
#     max_length = len(s[0])
#     res = ''
#     for x in s:
#         if len(x) > max_length:
#             res = x
#
#     return res
#
#
# def topTwo(l):
#     return sorted(l, reverse=True)[:2]
#
#
# l = [1, 4, 2, 3, 9, 1]
# m = findMax(l)
# print(m)
#
# n = topTwo(l)
# print(n)
#
# s = 'This is a information test'
# ss = s.split(' ')
# print(findLongest(ss))


# import string
#
#
# def top_two(l):
#     set(l)
#     l.sort(reverse=True)
#     m = l[0:2]
#
#
#     b = [str(i) for i in m]
#     return ','.join(b)
#
# l = [12, 34, 56, 78, 56]
#
# # because of no return value of top_two
# # c value will be None
# c = top_two(l)
# # print none is none
# print(c)


def extract_extension(fileName):
    # write your code here
    if fileName.rfind(".") > 0:
        rindex = fileName.rfind(".")
        return fileName[rindex + 1:]
    else:
        return " "


def extract_extension2(fileName):
    l = fileName.split('.')
    last = l[-1]
    if last == fileName:
        return " "
    else:
        return last


def extract_extension3(fileName):
    try:
        r_index = fileName.rindex('.')
        return fileName[r_index + 1:]
    except:
        return ' '


print(extract_extension3('information.txt'))
# output should be: txt
print(extract_extension3('My.heart.will.go.on.mp3'))
# output should be: mp3
print(extract_extension3('data.md'))
# output should be: md
print(extract_extension3('data'))
