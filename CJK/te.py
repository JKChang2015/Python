# te
# Created by JKChang
# 2019-03-08, 14:20
# Tag:
# Description: 

import pandas as pd

file = "/Users/jkchang/metabolights_zooma.tsv"
df = pd.read_csv(file,sep = '\t', header=0, encoding='utf-8')
print(df.shape)

da = df.drop_duplicates(subset='PROPERTY_VALUE', keep="last")
print(da.shape)

print()