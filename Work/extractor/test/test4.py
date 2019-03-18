# test4
# Created by JKChang
# 2019-03-15, 14:02
# Tag:
# Description: count each of individual techniques

import pandas as pd

df = pd.read_csv('../res/splited.tsv', sep = '\t')
count = df['Study Type'].value_counts(dropna=False).to_frame().reset_index()
count.columns=['Study Type','Counts']

full_names = pd.read_csv('../../resources/full name.csv')
name_pair = dict(zip(full_names['Study type'],full_names['Full Name']))
classify_pair = dict(zip(full_names['Study type'],full_names['Classify']))
count['Full name'] = count['Study Type'].map(name_pair)
count['Classify'] = count['Study Type'].map(classify_pair)


count.to_csv('../res/tech counts.tsv', sep = '\t',index=False)


print(df.columns)

