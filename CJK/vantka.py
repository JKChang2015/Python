# -*- coding: UTF-8 -*-
# File name: vantka
# Created by JKChang
# 01/03/2021, 22:50
# Tag:
# Description:

import pandas as pd

df = pd.read_csv('./resume.csv', encoding = 'latin-1')
df['class'] = df['class'].apply(lambda x: 1 if x == 'flagged' else 0)
print(pd.__version__)
