# Technologies
# Created by JKChang
# 2019-02-05, 09:34
# Tag:
# Description: 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def split(dataFrame, colName, sep):
    col = dataFrame.columns
    if colName not in col:
        print("Don't have column " + colName)
        return
    df_res = pd.DataFrame(columns=col)

    for index, row in dataFrame.iterrows():
        try:
            temp = row.copy()
            techniques = row[colName].split(sep)
            for technique in techniques:
                temp[colName] = technique
                df_res.loc[len(df_res)] = temp
        except:
            pass

    return df_res


def listOfStudy(dataFrame, onlyOneTech=False):  # list of files that contain one tech & more tech
    if onlyOneTech == True:
        one = dataFrame.groupby('ACC').filter(lambda x: len(x) == 1)
        return list(one.ACC)
    else:
        more = dataFrame.groupby('ACC').filter(lambda x: len(x) > 1)
        return sorted(list(set(more.ACC)))


def func(pct, allvals):
    absolute = int(pct / 100. * np.sum(allvals))
    return "{:.1f}%\n({:d})".format(pct, absolute)


def drawSimpleGraph(dataFrame, title):
    col = dataFrame.columns
    fig1, ax = plt.subplots()
    explode = (0, 0.1)
    # dataFrame[col[1]]
    wedges, texts, autotexts = ax.pie(dataFrame[col[1]], labels = dataFrame[col[0]], wedgeprops=dict(width=0.7), startangle=-20,
                                  autopct=lambda pct: func(pct, dataFrame[col[1]]))

    ax.axis('equal')
    ax.set_title(title)
    plt.show()


def drawRingGraph(dataFrame, title):
    pass

def mapCols(dataFrame, colName, newColName, namePair, fillna=False, naValue=''):
    # map colName with namepair and save in newColName
    dataFrame[newColName] = dataFrame[colName].map(namePair)
    if fillna == True:
        dataFrame[newColName] = dataFrame[colName].map(namePair, na_action=None)
        dataFrame = dataFrame.fillna(value=naValue)
        return dataFrame
    else:
        dataFrame[newColName] = dataFrame[colName].map(namePair)
        return dataFrame


def colCount(dataFrame, colName):
    res = dataFrame[colName].value_counts(dropna=False).to_dict()
    return res


df = pd.read_csv('./resources/MTBLS Curation Status Log.csv')
df = df.dropna(subset=['StudySize'])
df = split(df, colName='Technique', sep=';')

# ===========================================================================
# one = listOfStudy(df, onlyOneTech=True)
# more = listOfStudy(df)
# print(more)
# study_df = pd.DataFrame(columns=['Tech', 'Count'])
# study_df.loc[len(study_df)] = {'Tech': 'Only One', 'Count': len(one)}
# study_df.loc[len(study_df)] = {'Tech': 'More than One', 'Count': len(more)}
#
# drawSimpleGraph(study_df, 'Metabolights studies')

# ===========================================================================



# ==================== Full name mapping=================================
# names = pd.read_csv('./resources/full name.csv')
# namePair = dict(zip(names['Study type'], names['Full Name']))
# res_df = mapCols(dataFrame=df, colName='Technique',newColName='Full Name', namePair=namePair)
# ==================== group mapping =================================
# names = pd.read_csv('./resources/full name.csv')
# groupPair = dict(zip(names['Study type'], names['Classify']))
# namePair = dict(zip(names['Study type'], names['Full Name']))
# res_df = mapCols(dataFrame=df, colName='Technique', newColName='Group', namePair=groupPair)
# res_df = mapCols(dataFrame=res_df, colName='Technique', newColName='Full Name', namePair=namePair)
#
# res_df = res_df[['ACC', 'Technique', 'Full Name', 'Group']]

# =======================Count for each Group ==============================
# res = colCount(res_df,'Group')

# =======================Count for each Technique ==============================
res = colCount(df, 'Technique')
dff = pd.DataFrame.from_dict(res,orient='index')
dff.reset_index(level=0, inplace=True)
dff.columns = ['Technique', 'Counts']
names = pd.read_csv('./resources/full name.csv')
groupPair = dict(zip(names['Study type'], names['Classify']))
namePair = dict(zip(names['Study type'], names['Full Name']))
res_df = mapCols(dataFrame=dff, colName='Technique', newColName='Type', namePair=groupPair)
res_df = mapCols(dataFrame=res_df, colName='Technique', newColName='Full Name', namePair=namePair)

res_df = res_df[['Type','Counts','Technique','Full Name']]
res_df.to_csv('counted2.tsv', sep='\t', encoding='utf-8', index=False)
print()


#
#
# def ListOfStudy(filePath, onlyOneTech=False):  # list of file that contain one tech & more tech
#     df = split(filePath)
#     if onlyOneTech == True:
#         one = df.groupby('ACC').filter(lambda x: len(x) == 1)
#         return list(one.ACC)
#     else:
#         more = df.groupby('ACC').filter(lambda x: len(x) > 1)
#         return sorted(list(set(more.ACC)))


# path = './resources/MTBLS Curation Status Log.csv'
# one = ListOfStudy(filePath=path, onlyOneTech=True)
# more = ListOfStudy(filePath=path, onlyOneTech=False)
#
# my_df  = pd.DataFrame(columns = ['Tech','Count'])
# my_dic = {'Tech':'Only One', 'Count':len(one)}
# my_df.loc[len(my_df)] = my_dic
# my_dic = {'Tech':'more than One', 'Count':len(more)}
# my_df.loc[len(my_df)] = my_dic
#
# # my_df.to_csv('onlyOne.tsv', sep='\t', encoding='utf-8', index=False)
#
# drawSimpleGraph(my_df,'Metabolights Study Techniques')

# def countTech(filePath):
#     df = split()
#     df_count = df_split['Technique'].value_counts()
#     df_count = df_count.to_frame().reset_index()
#     df_count.columns = ['Technique', 'Count']
#
#
# def mapFullName(filePath, fullNameFile):
#     df = split(filePath)
#     names = pd.read_csv(fullNameFile)
#     name_pair = dict(zip(names['Study type'], names['Full Name']))
#     df['Full Name'] = df['Technique'].map(name_pair)
