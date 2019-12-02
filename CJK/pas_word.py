# pas_word
# Created by JKChang
# 29/11/2019, 11:17
# Tag:
# Description: 

import random
import string

d = string.digits
low = string.ascii_lowercase
up = string.ascii_uppercase
p = string.punctuation


def check_avaliable(s):
    if any({*s} & {*d}) == False:
        print('Please contain a digit')
        return False
    elif any({*s} & {*low}) == False:
        print('Please contain a lower letter')
        return False
    elif any({*s} & {*up}) == False:
        print('Please contain a upper letter')
        return False
    elif any({*s} & {*p}) == False:
        print('Please contain a punctuation')
        return False
    else:
        print('Thank you for your password')
        return True


def psw_genertate():
    length = random.choice(range(5, 16))
    res = []
    res.append(random.choice(d))
    res.append(random.choice(low))
    res.append(random.choice(up))
    res.append(random.choice(p))
    res += random.sample(set(d + low + up + p), length - len(res))
    random.shuffle(res)

    return ''.join(res)


i = 0
while (i < 10):
    ps = psw_genertate()
    print(ps)
    check_avaliable(ps)
    i += 1
