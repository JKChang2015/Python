import random
import os
import urllib.request, urllib.parse, urllib.error
import time

# 25April
# Created by JKChang
# 25/04/2017, 09:58
# Description: reviewing


#------------------------List-----------------------------

# #adding----------------
#
# myTeacher = 'ziming'
# another_list = ['a', 'b']
# my_list = [5, 10, 23.76, 'Hello', myTeacher, 7, another_list]
#
# print my_list
#
# my_list.append('First')
# print my_list
#
# my_list.insert(0, 'Third')
# print my_list
#
# #Slicing----------
# my_list = [5, 23.76, 'Hello',  ['new', 'list']]
#
# print my_list[1]
# print type(my_list[1])
#
# print my_list[-1]
# print type(my_list[-1])
#
# new_list= my_list[:5]
# print new_list
# print type(new_list)
#
# #Modify-----------
# my_list = [5, 23.76, 'Hello',  ['new', 'list']]
#
# my_list[0] = 'very begining'
# print my_list
#
# #Deleting---------
# my_list = [5, 23.76, 'Hello',  ['new', 'list']]
# my_list.remove('Hello')
# print my_list
#
# del my_list[1]
# print my_list
#
# last = my_list.pop()
# print my_list
# print last
#
# my_list = [5, 23.76, 'Hello',  ['new', 'list']]
# some = my_list.pop(0)
# print some
# print my_list

# Searching -----------
my_list = [5, 23.76, 'Hello',  ['new', 'list']]
num = input('please input a number')
if num in my_list:
    print('the number is in the list')
else:
    print('the number is NOT in the list')




#---------------------multiple loops -----------------------------
# numBlock = int(raw_input('pls input Blocks '))
# numLine = int(raw_input('pls input Line number per Block '))
# numStar = int(raw_input('pls input Star number per Line '))
#
# for i in range(numBlock):
#     for j in range(numLine):
#         for k in range(numStar):
#             print '*',
#         print
#     print


# ---------------------Multiplication table ---------------------

# for i in range (1, 10):
#     for j in range (1, 10):
#         if (j <= i ):
#             print j , 'x', i, '=', j*i, '\t',
#     print
# ------------------------Countdown timer------------------------------------
# t = 5
# for i in range (t, 0, -1):
#     print i
#     time.sleep(1)
# print '__finished! '

# -------------------------LOOP---------------------------------------------
# for looper in [1,2,3,4,5]:
#     print looper , 'Hello'
# print
#
# for looper in range (1,5):
#     print looper, "Hi"
# print
#
# for looper in range (1, 10, 2):
#     print looper, "Bye"
# print
#
# for looper in range (4):
#     print looper, 'whatever'

# ------------------------ read local file ---------------------------------

# path = os.getcwd() + "/resources/test.txt"
# print open(path, 'r+').read()

# ------------------------ read text from web site -------------------------
# file = urllib.urlopen('http://helloworldbook.com/data/message.txt')
# message = file.read()
# print message

# ------------------temperature converter-----------------------------------

# print 'This program is converts Fahrenheit to Celsius'
# fahrenheit = float(raw_input('pls in put a temperature in fahrenheit: '))
# celsius = (fahrenheit - 32) * 5 /9
# print 'That is ', celsius, 'Degree'


# -----------------------raw input -----------------------------------------

# someone = raw_input('pls input your name: ')
# print 'Hello', someone

# -----------------Guess a random number -----------------------------------
# start = 1
# end = 99
#
# secret = random.randint(start, end)
# guess = 0
# tries = 0
#
# print "It's a number between", start, 'and', end, ", I will give you 7 tries"
#
# while guess != secret and tries < 7:
#     guess = input('what is your guess? ')
#     if guess < secret:
#         print 'too low'
#     elif guess > secret:
#         print 'too high'
#     tries += 1
#
# if guess == secret:
#     print 'You got it'
# else:
#     print 'finished'
