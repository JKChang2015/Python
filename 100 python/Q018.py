# Q018
# Created by JKChang
# 28/02/2017, 11:35
# Tag: password checking
# Description: A website requires the users to input username and password to register. Write a program to check the
#              validity of password input by users.
#
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
#     Passwords that match the criteria are to be printed, each separated by a comma.
#
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

import re

while True:
    s = raw_input('Password: ')
    if not s:
        break

    if not re.search('[a-z]', s):
        print 'ERROR: At least 1 letter between [a-z]'
        continue

    if not re.search('[0-9]', s):
        print 'ERROR: At least 1 number between [0-9]'
        continue

    if not re.search('[A-Z]', s):
        print 'ERROR: At least 1 letter between [A-Z]'
        continue

    if not re.search('[$#@]', s):
        print 'ERROR: At least 1 symbol in [$#@]'
        continue

    if len(s) < 6 or len(s) > 12:
        print 'ERROR: length should between 6 to 12 '
        continue
    else:
        print "Well done! your password is: ", s
        break
