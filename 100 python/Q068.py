# 068
# Created by JKChang
# 09/05/2017, 14:32
# Tag: generator & yield
# Description: Please write a program using generator to print the even numbers between 0 and n in comma separated
#              form while n is input by console.
#
# Example:
# If the following n is given as input to the program:
#
# 10
#
# Then, the output of the program should be:
#
# 0,2,4,6,8,10
#

def Generator(n):
    for i in range(n+1):
        if i%2 ==0:
            yield i

s = int(input())
print(','.join(str(x) for x in Generator(s)))


# Method 2
# print ','.join([str(x) for x in range(int(raw_input()) + 1) if x % 2 == 0])

# Method 3
# n = int(raw_input('Input: '))
# res = []
# for i in range (n+1):
#     if i % 2 ==0:
#         res.append(str(i))
#
# print ','.join(res)
