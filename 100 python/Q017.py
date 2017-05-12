# Q017
# Created by JKChang
# 28/02/2017, 11:33
# Tag: 
# Description: Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.
#
# Example: Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

import sys

res = 0

while True:
    s = raw_input(" 'D' for deposit and 'W' for withdrawal: ")
    if not s:
        break

    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])

    if operation == "D":
        res += amount
    elif operation == "W":
        res -= amount
    else:
        pass

print res
