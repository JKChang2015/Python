# -*- coding: UTF-8 -*-
# File name: hackerrank
# Created by JKChang
# 15/07/2020, 13:29
# Tag:
# Description: 

# def count_substring(s, sub_string):
# #     count = 0
# #     for i in range(0, len(s) - len(sub_string) + 1):
# #         if sub_string == s[i: i + len(sub_string)]:
# #             count += 1
# #     return count

# def count_substring(s, sub_string):
#     count = 0
#     for i in range(len(s)):
#         if s[i:].startswith(sub_string):
#             count += 1
#     return count
#
#
# def wrap(string, max_width):
#     res = []
#     for i in range(0,len(string), max_width):
#         res.append(string[i:i+max_width])
#     return '\n'.join(res)
#
# s = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
# print(wrap(s,4))
#
# def solve(s):
#     res = [x if x[0].isdigit() else x.title() for x in s.split(' ')]
#     return ' '.join(res)

# def solve(s):
#     l = s.split(' ')
#     res = []
#     for x in l:
#         if en(x) < 1 or x[0].isdigit():
#             res.append(x)
#         else:
#             res.append(x.title())
#     return ' '.join(res)
#
# s = 'hello   world  lol'
# print(solve(s))
# import calendar
# print(calendar.TextCalendar(firstweekday=6).formatyear(2015))

# import itertools
#
# if __name__ == '__main__':
#     c, div = [int(x) for x in input().split()]
#     nums = []
#     for i in range(c):
#         nums.append([int(x) for x in input().split()])
#
#     com = list(itertools.product(*nums))
#     res = []
#     for prod in com:
#         res.append(sum(map(lambda i: i * i, prod)) % div)
#     print(max(res))

# def score_words(words):
#     res = 0
#     for word in words:
#         vowels = [x for x in word if x.lower() in ['a','e','i','o','u','y']]
#         if len(vowels) > 0:
#             v_s = 2 if len(vowels)%2==0 else 1
#         else:
#             v_s = 0
#         res += v_s
#     return res
#
#
# n = int(input())
# words = input().split()
# print(score_words(words))

from itertools import permutations

if __name__ == '__main__':
    n = int(input())
    ele = input().split()
    num = int(input())

    per = list(permutations(ele,num))
    contain = 0
    for x in per:
        if 'a' in x:
            contain += 1
    print(contain/len(per))
