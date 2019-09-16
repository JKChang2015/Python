# organism
# Created by JKChang
# 2019-03-27, 14:39
# Tag:
# Description: extract organism from each of study sample file



from Work.extractor import fileReader, studyList
import pandas as pd

studyIDs = studyList.getStudyIDs()

print(len(studyIDs))

folderPath = r'/Volumes/GoogleDrive/My Drive/study_metadata_backup/'
res = []



for studyID in studyIDs:
    print(studyID)
    studyPath = folderPath + studyID + '/'
    try:
        sample_list = fileReader.investigation_local_reader(studyID,['Study File Name'])
        organism = []

        for sample in sample_list:
            filename = sample['Study File Name']
            filePath = studyPath + filename
            try:
                organism += list(set(fileReader.sample_reader(filePath,'Characteristics[Organism]')))
            except:
                organism += list(set(fileReader.sample_reader(filePath, 'Characteristics[organism]')))
            organism = list(set(organism))


        if len(organism) >= 1:
            temp = ','.join(organism)
            res.append({'studyID':studyID, 'organism': temp})
        else:
            print(studyID + '《=========')
    except:
        print('fail to open ' + studyID)


df = pd.DataFrame(res)

df = df[['studyID','organism']]

df_split = pd.DataFrame(columns=['studyID', 'organism'])

# split the Techniques into different rows
for index, row in df.iterrows():
    try:
        temp = row.copy()
        organisms = row['organism'].split(',')
        for organism in organisms:
            temp['organism'] = organism
            df_split.loc[len(df_split)] = temp
    except:
        pass

df_split = df_split.drop(index = df_split[df_split['organism'].isin(['blank','reference compound'])].index)


df_split.to_csv('organismss.tsv',sep='\t',index=False)

