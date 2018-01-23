# -*- coding: UTF-8 -*-
# left_visual
# Created by JKChang
# 23/01/2018, 06:27
# Tag:
# Description: left staff data visualization

import matplotlib
import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv(r'./resources/HR_comma_sep.csv')
data = data.rename(columns={'sales': 'Departments'})

onJob = data[data['left'] == 0]
leftJob = data[data['left'] == 1]

print('Num of on job staffs: {}, - {:.2%}'.format(len(onJob), len(onJob) / len(data)))
print('Num of left job staffs: {}, - {:.2%}'.format(len(leftJob), len(leftJob) / len(data)))

staff = data.left.value_counts()
pandas.DataFrame({'On': [staff[0]], 'Left': [staff[1]]})

plt.figure(dpi=128, figsize=(10, 10))
plt.title('On Job & Left Job', fontsize=30)
plt.axis('equal')
font = {'size': 20}

matplotlib.rc('font', **font)
explode = (0, 0.05)
plt.pie(staff, explode=explode, labels=['On Job', 'Left Job'], autopct='%.2f%%', startangle=90)
plt.savefig('results/left_overview.png', bbox_inches='tight')
plt.show()
