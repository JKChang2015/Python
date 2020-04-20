# target
# Created by JKChang
# 2019-02-11, 13:28
# Tag:
# Description:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def func(pct, allvals):
    absolute = int(pct / 100. * np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)


def drawSimpleGraph(dataFrame, title):
    col = dataFrame.columns
    fig1, ax = plt.subplots()
    explode = (0, 0.1)
    # dataFrame[col[1]]
    wedges, texts, autotexts = ax.pie(dataFrame[col[1]], labels=dataFrame[col[0]], wedgeprops=dict(width=0.7),
                                      startangle=-100,
                                      autopct=lambda pct: func(pct, dataFrame[col[1]]))

    ax.axis('equal')
    ax.set_title(title)
    plt.show()


df = pd.read_csv('./results/target.tsv', sep='\t')

conditions = [
    (df['iri'].isnull()) & (df['type'].str.contains('untargeted')),
    (df['iri'].isnull()) & ('untargeted' not in df['type']),
    (df['iri'].notnull())]

choices = ['Untargeted', 'Un-mapped', 'Targeted']
df['targeted?'] = np.select(conditions, choices)

result = []
studyIDs = df['studyID'].unique()

dff = pd.DataFrame(columns=['studyID', 'target', 'untargeted', 'un-mapped'])

for studyID in studyIDs:
    temp = df[df['studyID'] == studyID]
    res = temp['targeted?'].value_counts(dropna=False).to_dict()
    res['studyID'] = studyID
    dff = dff.append(res, ignore_index=True)

dff.to_csv('targeted for each study.tsv', sep='\t', index=False)

# df.to_csv('target.tsv', sep='\t', index=False)

# ================ Count target ===========
res = df['targeted?'].value_counts(dropna=False).to_dict()
res = pd.DataFrame.from_dict(res, orient='index')
res.reset_index(level=0, inplace=True)
res.columns = ['status', 'Counts']

res.to_csv('target count.tsv', sep='\t', index=False)

drawSimpleGraph(res,'Targeted vs Un-target')
# ===========================================


# df.to_csv('target2.tsv', sep='\t', index=False)
