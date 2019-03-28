# organism
# Created by JKChang
# 2019-03-27, 14:39
# Tag:
# Description: extract organism from each of study sample file



from Work.extractor import fileReader, studyList
import pandas as pd

studyIDs = studyList.getStudyIDs(publicStudy=True)

print(len(studyIDs))

folderPath = r'/Volumes/GoogleDrive/My Drive/study_metadata_backup/'
res = []



for studyID in studyIDs:
    # print(studyID)
    studyPath = folderPath + studyID + '/'
    sample_list = fileReader.investigation_reader(studyID,['Study File Name'])
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
        print(studyID)


df = pd.DataFrame(res)
df = df[['studyID','organism']]

df.to_csv('organism.tsv',sep='\t',index=False)

