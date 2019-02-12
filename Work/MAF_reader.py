# MAF_reader
# Created by JKChang
# 2019-02-11, 20:43
# Tag:
# Description: read MAF file

import os
import pandas as pd

path = '/Volumes/GoogleDrive/My Drive/study_metadata_backup/MTBLS29'

address = []

for file in os.listdir(path):
    if file.endswith("maf.tsv"):
        address.append(os.path.join(path, file))

for ad in address:
    df = pd.read_csv(ad,sep='\t')
    print(df.head())