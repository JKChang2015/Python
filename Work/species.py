# species
# Created by JKChang
# 09/07/2018, 16:10
# Tag:
# Description:  extract species from curation study spreadsheets

import operator
from collections import Counter
import csv
import pandas as pd

pd = pd.read_csv(r'./resources/MTBLS Curation Status Log - Studies.csv')

species = pd.Species.dropna()

flat = []
for sp in species:
    if ';' in sp:
        flat = flat + sp.split(';')
    elif '/' in sp:
        flat = flat + sp.split('/')
    elif ',' in sp:
        flat = flat + sp.split(',')
    else:
        flat.append(sp)

flat = [x for x in flat if len(x) > 0]

res = dict(Counter(flat))
res = dict(sorted(res.items(), key=operator.itemgetter(1), reverse=True))

with open('./results/species.csv','w') as f:
    w = csv.writer(f)
    w.writerow(['species', 'occurance'])
    w.writerows(res.items())