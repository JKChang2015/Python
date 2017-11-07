# ts
# Created by JKChang
# 07/11/2017, 14:46
# Tag:
# Description: 
#
# def reverse(arr,start, end):
#     while start < end:
#         arr[start], arr[end] = arr[end],arr[start]
#         start += 1
#         end -= 1
#     return arr
#
# arr = [1,2,4,3]
# end = len(arr) -1
# print(reverse(arr,0,end))

import sys

#
# def reverse(ar, start, end):
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         # print(arr)
#         start += 1
#         end -= 1
#     return arr
#
#
# n = int(input().strip())
# arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# print(' '.join(str(x) for x in reverse(arr,0 , n-1)))

# def test(n):
#     if n % 2 == 0:
#         print('Weird')
#     elif 2 <= n <= 5:
#         print("Not Weird")
#     elif 6 <= n <= 20:
#         print('Weird')
#     elif n > 20:
#         print("Not Weird")

# n = int(input())
# for i in range(n):
#     print(n ** 2)