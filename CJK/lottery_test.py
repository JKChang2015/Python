# lottery_test
# Created by JKChang
# 09/10/2019, 10:57
# Tag:
# Description:

from CJK.lottery import *


def test_set_for_life():
    a = 0
    res_num = [17, 25, 29, 33, 41]
    res_star = 2
    tab = {'2 MAIN NUMBERS': 0,
           '2 MAIN NUMBERS WITH LIFE BALL': 0,
           '3 MAIN NUMBERS': 0,
           '3 MAIN NUMBERS WITH LIFE BALL': 0,
           '4 MAIN NUMBERS': 0,
           '4 MAIN NUMBERS WITH LIFE BALL': 0,
           '5 MAIN NUMBERS': 0,
           '5 MAIN NUMBERS WITH LIFE BALL': 0,
           'SORRY': 0
           }

    while (a < 1000000):
        num, star = set_for_life()
        # print(list(num) + list(star), end=' ')

        if len(set(res_num).intersection(set(num))) == 2 and res_star != star[0]:
            tab['2 MAIN NUMBERS'] += 1
            print('2 MAIN NUMBERS')

        elif len(set(res_num).intersection(set(num))) == 2 and res_star == star[0]:
            tab['2 MAIN NUMBERS WITH LIFE BALL'] += 1
            print('2 MAIN NUMBERS WITH LIFE BALL')

        elif len(set(res_num).intersection(set(num))) == 3 and res_star != star[0]:
            tab['3 MAIN NUMBERS'] += 1
            print('3 MAIN NUMBERS')

        elif len(set(res_num).intersection(set(num))) == 3 and res_star == star[0]:
            tab['3 MAIN NUMBERS WITH LIFE BALL'] += 1
            print('3 MAIN NUMBERS WITH LIFE BALL')

        elif len(set(res_num).intersection(set(num))) == 4 and res_star != star[0]:
            tab['4 MAIN NUMBERS'] += 1
            print('4 MAIN NUMBERS')

        elif len(set(res_num).intersection(set(num))) == 4 and res_star == star[0]:
            tab['4 MAIN NUMBERS WITH LIFE BALL'] += 1
            print('4 MAIN NUMBERS WITH LIFE BALL')

        elif len(set(res_num).intersection(set(num))) == 5 and res_star != star[0]:
            tab['5 MAIN NUMBERS'] += 1
            print('5 MAIN NUMBERS')

        elif len(set(res_num).intersection(set(num))) == 5 and res_star == star[0]:
            tab['5 MAIN NUMBERS WITH LIFE BALL'] += 1
            print('5 MAIN NUMBERS WITH LIFE BALL')

        else:
            tab['SORRY'] += 1
            # print('Sorry')

        a += 1

    print('--' * 30)
    for v, i in tab.items():
        print(v, i)


def test_euromillions():
    a = 0
    res_num = [7, 10, 15, 44, 49]
    res_star = [3,12]
    tab = {'2 MAIN NUMBERS': 0,
           '2 MAIN NUMBERS and 1 LUCKY STARS': 0,
           '1 MAIN NUMBERS and 2 LUCKY STARS': 0,

           '3 MAIN NUMBERS': 0,
           '3 MAIN NUMBERS and 1 LUCKY STARS': 0,
           '2 MAIN NUMBERS and 2 LUCKY STARS': 0,

           '4 MAIN NUMBERS': 0,
           '3 MAIN NUMBERS and 2 LUCKY STARS': 0,
           '4 MAIN NUMBERS and 1 LUCKY STARS': 0,
           '4 MAIN NUMBERS and 2 LUCKY STARS': 0,

           '5 MAIN NUMBERS': 0,
           '5 MAIN NUMBERS and 1 LUCKY STARS': 0,
           '5 MAIN NUMBERS and 2 LUCKY STARS': 0,

           'SORRY': 0
           }

    while (a < 1000000):
        num, star = euromillions()
        # print(list(num) + list(star), end=' ')

        if len(set(res_num).intersection(set(num))) == 2 and len(set(res_star).intersection(set(star))) == 0:
            tab['2 MAIN NUMBERS'] += 1
            print('2 MAIN NUMBERS')

        elif len(set(res_num).intersection(set(num))) == 2 and len(set(res_star).intersection(set(star))) == 1:
            tab['2 MAIN NUMBERS and 1 LUCKY STARS'] += 1
            print('2 MAIN NUMBERS and 1 LUCKY STARS')


        elif len(set(res_num).intersection(set(num))) == 1 and len(set(res_star).intersection(set(star))) == 2:
            tab['1 MAIN NUMBERS and 2 LUCKY STARS'] += 1
            print('1 MAIN NUMBERS and 2 LUCKY STARS')



        elif len(set(res_num).intersection(set(num))) == 3 and len(set(res_star).intersection(set(star))) == 0:
            tab['3 MAIN NUMBERS'] += 1
            print('3 MAIN NUMBERS')


        elif len(set(res_num).intersection(set(num))) == 3 and len(set(res_star).intersection(set(star))) == 1:
            tab['3 MAIN NUMBERS and 1 LUCKY STARS'] += 1
            print('3 MAIN NUMBERS and 1 LUCKY STARS')

        elif len(set(res_num).intersection(set(num))) == 2 and len(set(res_star).intersection(set(star))) == 2:
            tab['2 MAIN NUMBERS and 2 LUCKY STARS'] += 1
            print('2 MAIN NUMBERS and 2 LUCKY STARS')


        elif len(set(res_num).intersection(set(num))) == 4 and len(set(res_star).intersection(set(star))) == 0:
            tab['4 MAIN NUMBERS'] += 1
            print('4 MAIN NUMBERS')

        elif len(set(res_num).intersection(set(num))) == 3 and len(set(res_star).intersection(set(star))) == 2:
            tab['3 MAIN NUMBERS and 2 LUCKY STARS'] += 1
            print('3 MAIN NUMBERS and 2 LUCKY STARS')


        elif len(set(res_num).intersection(set(num))) == 4 and len(set(res_star).intersection(set(star))) == 1:
            tab['4 MAIN NUMBERS and 1 LUCKY STARS'] += 1
            print('4 MAIN NUMBERS and 1 LUCKY STARS')

        elif len(set(res_num).intersection(set(num))) == 4 and len(set(res_star).intersection(set(star))) == 2:
            tab['4 MAIN NUMBERS and 2 LUCKY STARS'] += 1
            print('4 MAIN NUMBERS and 2 LUCKY STARS')


        elif len(set(res_num).intersection(set(num))) == 5 and len(set(res_star).intersection(set(star))) == 0:
            tab['5 MAIN NUMBERS'] += 1
            print('5 MAIN NUMBERS')

        elif len(set(res_num).intersection(set(num))) == 5 and len(set(res_star).intersection(set(star))) == 1:
            tab['5 MAIN NUMBERS and 1 LUCKY STARS'] += 1
            print('5 MAIN NUMBERS and 1 LUCKY STARS')


        elif len(set(res_num).intersection(set(num))) == 5 and len(set(res_star).intersection(set(star))) == 2:
            tab['5 MAIN NUMBERS and 2 LUCKY STARS'] += 1
            print('5 MAIN NUMBERS and 2 LUCKY STARS')

        else:
            tab['SORRY'] += 1
            # print('Sorry')

        a += 1

    print('--' * 30)
    for v, i in tab.items():
        print(v, i)


test_euromillions()