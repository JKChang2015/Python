# die_visual
# Created by JKChang
# 22/01/2018, 14:43
# Tag:
# Description: die visualization

import pygal

from RD_Club.Pro2.die import Die

die = Die()
res = []

# rolling die for 10000 times
for roll_number in range(10001):
    re = die.roll()
    res.append(re)

# calculate frequencies
frequencies = []
for value in range(1, die.num_sies + 1):
    frequency = res.count(value)
    frequencies.append(frequency)

# draw histogram of frequencies
hist = pygal.Bar()

hist.title = 'Results of rolling one Die 10000 times.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist._x_title = 'Result'
hist._y_title = 'Frequency of result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
