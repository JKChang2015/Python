import random
import os
import urllib

# 25April
# Created by JKChang
# 25/04/2017, 09:58
# Description: reviewing



#-------------------------LOOP-------------------------------------
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

#------------------------ read local file --------------------------

# path = os.getcwd() + "/resources/test.txt"
# print open(path, 'r+').read()

#------------------------ read text from web site -------------------
# file = urllib.urlopen('http://helloworldbook.com/data/message.txt')
# message = file.read()
# print message

#------------------temperature converter-----------------------------------

# print 'This program is converts Fahrenheit to Celsius'
# fahrenheit = float(raw_input('pls in put a temperature in fahrenheit: '))
# celsius = (fahrenheit - 32) * 5 /9
# print 'That is ', celsius, 'Degree'


#-----------------------raw input -----------------------------------------

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
