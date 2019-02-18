# fileReader
# Created by JKChang
# 2019-02-15, 10:29
# Tag:
# Description: read investigation / assay / MAF file

import pandas as pd

import config


def investigation_reader(studyID, prefix):
    import re
    import paramiko

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    client.connect(config.SSH_PARAMS['host'], username=config.SSH_PARAMS['user'],
                   password=config.SSH_PARAMS['password'])
    sftp_client = client.open_sftp()
    address = '/net/isilonP/public/rw/homes/tc_cm01/metabolights/prod/studies/stage/private/' + studyID + '/i_Investigation.txt'
    try:
        with sftp_client.open(address) as f:
            for line in f.readlines():
                if line.startswith(prefix + '\t'):
                    content = list(re.findall(r'"([^"]*)"', line))  # extract content after prefix in " "
                    return content
    except:
        print('Fail to read investigation file from ' + studyID)


def assay_reader(filePath, colName, dropna=True):
    df = pd.read_csv(filePath, sep='\t')
    # return list of content in colName
    if dropna:
        return df[colName].dropna().tolist()
    else:
        return df[colName].tolist()


def MAF_reader(filePath, colName):
    pass
