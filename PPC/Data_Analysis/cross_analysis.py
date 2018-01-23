# cross_analysis
# Created by JKChang
# 23/01/2018, 07:45
# Tag:
# Description: 

import matplotlib.pyplot as plt
import pandas
import seaborn as sns

data = pandas.read_csv(r'./resources/HR_comma_sep.csv')
data = data.rename(columns={'sales': 'Departments'})


plt.figure()

sns.pairplot(data, hue='left', vars=['satisfaction_level', 'last_evaluation', 'average_montly_hours',
                                    'number_project', 'time_spend_company', 'Work_accident', 'promotion_last_5years',
                                     # 'Departments', 'salary'
                                     ])

plt.savefig('results/cross analysis.png', bbox_inches='tight')
plt.show()