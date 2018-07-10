# clean_tax
# Created by JKChang
# 10/07/2018, 20:22
# Tag:
# Description: clean taxinonemy urls

import pandas as pd

df = pd.read_csv('../test/temp.csv')
col = df['url'].dropna().drop_duplicates()
col.to_csv('../results/species_url.csv')
print(col)


