# Technologies
# Created by JKChang
# 2019-02-05, 09:34
# Tag:
# Description: 
import matplotlib.pyplot as plt
import pandas as pd


def split(filePath):
    import pandas as pd

    df = pd.read_csv(filePath)
    # drop some empty studies
    df = df.dropna(subset=['StudySize'])
    df_split = pd.DataFrame(columns=['ACC', 'StudySize', 'Status', 'Releasedate', 'SubmissionDate',
                                     'UserName', 'Technique', 'AccShort', 'StudyID', 'UpdateDate',
                                     'nmr_size', 'ms_size', 'Empty?', '150'])

    for index, row in df.iterrows():
        try:
            temp = row.copy()
            techniques = row['Technique'].split(';')
            for technique in techniques:
                temp['Technique'] = technique
                df_split.loc[len(df_split)] = temp
        except:
            pass

    return df_split


def drawSimpleGraph(dataFrame, title):
    col = dataFrame.columns
    fig1, ax = plt.subplots()
    explode = (0, 0.1)
    p, tx, autotexts = ax.pie(dataFrame[col[1]], explode=explode, labels=dataFrame[col[0]], autopct="", startangle=180)

    for i, a in enumerate(autotexts):
        a.set_text("{}".format(dataFrame[col[1]][i]))

    ax.axis('equal')
    ax.set_title(title)
    plt.show()


def ListOfStudy(filePath, onlyOneTech=False):  # list of file that contain one tech & more tech
    df = split(filePath)
    if onlyOneTech == True:
        one = df.groupby('ACC').filter(lambda x: len(x) == 1)
        return list(one.ACC)
    else:
        more = df.groupby('ACC').filter(lambda x: len(x) > 1)
        return sorted(list(set(more.ACC)))


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

def countTech(filePath):
    df = split()
    df_count = df_split['Technique'].value_counts()
    df_count = df_count.to_frame().reset_index()
    df_count.columns = ['Technique', 'Count']


def mapFullName(filePath, fullNameFile):
    df = split(filePath)
    names = pd.read_csv(fullNameFile)
    name_pair = dict(zip(names['Study type'], names['Full Name']))
    df['Full Name'] = df['Technique'].map(name_pair)
