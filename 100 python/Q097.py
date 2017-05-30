# Q097
# Created by JKChang
# 09/05/2017, 15:37
# Tag: permutation
# Description: Please write a program which prints all permutations of [1,2,3]

import itertools

print list(itertools.permutations([1,2,3]))
# li = [1,2,3]
# print list(itertools.combinations(li,3))

# stuff = [1, 2, 3]
# print itertools.combinations(stuff,3)
# for L in range(0, len(stuff)+1):
#   for subset in itertools.combinations(stuff, L):
#     print(subset)