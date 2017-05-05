# Q046
# Created by JKChang
# 28/04/2017, 14:59
# Description: Write a program which can map() to make a list whose elements are square of elements in
#              [1,2,3,4,5,6,7,8,9,10].

# MAP applies a function to all the items in an input_list. Here is the blueprint:
# map(function_to_apply, list_of_inputs)

# lambda is a quick def

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squareNm = map(lambda x: x ** 2, li)
print squareNm