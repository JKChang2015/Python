# HR
# Created by JKChang
# 23/01/2018, 05:58
# Tag:
# Description: HR investigation

import pandas
from pandas import DataFrame as df


data = pandas.read_csv(r'./resources/HR_comma_sep.csv')
print(data.info())
print(data.describe())
# data.describe().to_csv('results/data_describe.csv', encoding='utf-8')

