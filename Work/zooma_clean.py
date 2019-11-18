# zooma_clean
# Created by JKChang
# 14/11/2019, 15:39
# Tag:
# Description: 

import pandas as pd

df = pd.read_csv('./resources/metabolights_zooma.tsv',sep = '\t')
df = df.drop_duplicates(subset=['PROPERTY_TYPE','PROPERTY_VALUE'])
df.to_csv('./resources/metabolights_zooma.tsv', sep='\t', index=False)

print()


