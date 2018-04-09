# R012
# Created by JKChang
# 01/03/2017, 12:18
# Tag: Prime number
# Description: prime number between(101,200)

for num in range(101, 201):
    prime = True
    for pn in range(2, num):
        if (num % pn == 0):
            prime = False
            break
    if prime:
        print(num)

