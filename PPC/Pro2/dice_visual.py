# dice_visual
# Created by JKChang
# 22/01/2018, 15:04
# Tag:
# Description: 
import pygal

from PPC.Pro2.die import Die

die_1 = Die()
die_2 = Die(10)

res = []
for roll_num in range(1000):
    re = die_1.roll() + die_2.roll()
    res.append(re)

frequencies = []
max_result = die_1.num_sies + die_2.num_sies
for value in range(2, max_result + 1):
    frequency = res.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Result of rolling two D6 dice 1000 times'
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
