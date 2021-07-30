# sina
# Created by JKChang
# 14/04/2018, 18:12
# Tag:
# Description:

# -*- coding: utf-8 -*-
import requests
import json
import time
import pymongo
import csv
import os
import codecs
import sys


client = pymongo.MongoClient('localhost', 27017)
weibo = client['weibo']
comment_ = weibo['comment_']

headers = {
    "Cookies":'_T_WM=6d0295e4480e94a5a5ad6f9aaa534922; SCF=ArvL2gmHRcZ1QuCUNOIl9RKSfdfgFC_QNiGcwcBue5BlvBcaNLf85lFjEd9apUFGbNlo-jIlwLgNzo2y-_S8VcA.; H5_INDEX_TITLE=%E8%8C%AA_%E8%8C%AA; H5_INDEX=3; WEIBOCN_FROM=1110006030; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D102803_ctg1_8999_-_ctg1_8999_home%26featurecode%3D20000320%26oid%3D4228795424767840%26uicode%3D20000061%26fid%3D4228795424767840; SUB=_2A25317VtDeRhGedG6VcS-S7IzDmIHXVVO9slrDV6PUJbkdBeLWynkW1NUUzFhVcNiS6S356n-KSlYps43d5uUFEH; SUHB=0N20ObKDtzoMge; SSOLoginState=1523828029',
    "User-Agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}
# id可以换成任意新浪微博的微博id号，具体可以打开相应微博查看，这个评论通过微博开放的api获取，不是微博地址
url_comment = ['https://m.weibo.cn/api/comments/show?id=4173028302302955&page={}'.format(str(i)) for i in range(1,1000)]
#print(url_comment)




path = os.getcwd()+"/weibo.csv"
csvfile = open(path, 'w')
csvfile.write(codecs.BOM_UTF8)
writer = csv.writer(csvfile)
#writer.writerow(('username','created_at','source','comment','like_counts'))

def get_comment(url):
    try:
        wb_data = requests.get(url,headers=headers)
        #data_comment = json.loads(wb_data)
        #print(data_comment)
        jsondata = wb_data.json()
        datas = jsondata.get('data').get('data')
        for data in datas:
            created_at = data.get("created_at")
            like_counts = data.get("like_counts")
            source = data.get("source")
            username = data.get("user").get("screen_name")
            comment = data.get("text")
            #print json.dumps(comment, encoding="UTF-8", ensure_ascii=False)
            writer.writerow((username,created_at,source,json.dumps(comment, encoding="UTF-8", ensure_ascii=False),like_counts))
    except KeyError:
        pass
for url in url_comment:
    get_comment(url)
    time.sleep(2)