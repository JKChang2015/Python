# organism2
# Created by JKChang
# 2019-03-28, 10:43
# Tag:
# Description: 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from Work.extractor import fileReader

def func(pct, allvals):
    absolute = int(pct / 100. * np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)


def drawSimpleGraph(dataFrame, title):
    col = dataFrame.columns
    fig1, ax = plt.subplots()
    explode = (0, 0.1)
    wedges, texts, autotexts = ax.pie(dataFrame[col[1]], labels=dataFrame[col[0]], wedgeprops=dict(width=0.7),
                                      startangle=-20,
                                      autopct=lambda pct: func(pct, dataFrame[col[1]]))

    ax.axis('equal')
    ax.set_title(title)
    plt.savefig(title + '.png', dpi=100)
    plt.show()



df = pd.read_csv('organism.tsv', sep='\t')
count = df['organism'].value_counts().nlargest(n=15)
organisms = list(count.keys())

oc = 0

for organism in organisms:
    oc += 1
    print('extract ' + organism + ' ....')
    study_list = df[df['organism'] == organism]['studyID'].tolist()
    factorName = []
    factorType = []
    for studyID in study_list:
        print(studyID)
        results = fileReader.investigation_reader(studyID, ['Study Factor Name', 'Study Factor Type'])
        for result in results:
            factorName.append(result['Study Factor Name'])
            factorType.append(result['Study Factor Type'])

    factorName = [x.title() for x in factorName]
    factorType = [x.title() for x in factorType]

    nameCount = []
    typeCount = []

    for term in set(factorName):
        nameCount.append({'term': term, 'count': factorName.count(term)})

    for term in set(factorType):
        typeCount.append({'term': term, 'count': factorType.count(term)})

    if len(nameCount) > 0:
        nameresult = pd.DataFrame(nameCount).sort_values(by=['count'], ascending=False)
        nameresult = nameresult[['term','count']]
        drawSimpleGraph(nameresult.head(8), organism + ' Name count')
        nameresult.to_csv('organism results/' + str(oc) + '. ' + organism + ' Factor Name.tsv', sep='\t', index=False)

    if len(typeCount) > 0:
        typeresult = pd.DataFrame(typeCount).sort_values(by=['count'], ascending=False)
        typeresult = typeresult[['term', 'count']]
        drawSimpleGraph(typeresult.head(8), organism + ' Type count')
        typeresult.to_csv('organism results/' + str(oc) +'. ' + organism + ' Factor Type.tsv', sep='\t', index=False)