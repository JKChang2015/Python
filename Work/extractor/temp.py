# temp
# Created by JKChang
# 2019-03-27, 16:22
# Tag:
# Description: 

import pandas as pd
filePath = r'/Volumes/GoogleDrive/My Drive/study_metadata_backup/MTBLS177/s_DDA_PI.txt'
df = pd.read_csv(filePath,sep='\t')
print(df.columns)
a = df['Characteristics[organism]']
a = df['Characteristics[Organism]']
print(a)