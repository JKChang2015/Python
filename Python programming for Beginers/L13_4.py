# L13_4
# Created by JKChang
# 17/02/2017, 11:55
# Description: function with return a value

def calTax(price, tax_rate):
    total = price + (price * tax_rate)
    return total

my_price = float(input('pls input a price: '))
totalPrice = calTax(my_price, 0.06)

print(str(totalPrice))

