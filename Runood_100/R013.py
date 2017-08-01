# -*- coding: UTF-8 -*-
# R013
# Created by JKChang
# 01/03/2017, 14:26
# Tag: Narcissistic number
# Description: Narcissistic number  打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：
#              153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

for n in range(100, 1000):
    # 找到一个数的百位／十位 和 个位
    i = n / 100
    j = n / 10 % 10
    k = n % 10

    if n == i ** 3 + j ** 3 + k ** 3:
        print(n)
