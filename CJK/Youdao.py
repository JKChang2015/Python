# -*- coding: utf-8 -*-
# Youdao
# Created by JKChang
# 30/05/2017, 18:46
# Tag: regular expression
# Description: convert Youdao terms to tsv format

import re
import io

youdaoPath = '/Users/jkchang/Downloads/1.txt'
dict ={} #{english, chinese}

with open(youdaoPath) as f:
    for line in f:
        if line[0].isdigit():
            nextline = f.next()
            pat = "(\d+)\,\s+(\w+)\s+(.*)"
            res = re.match(pat, line)
            dict[res.group(2).strip().capitalize()] = nextline.strip()

with io.open('/Users/jkchang/Downloads/3.txt','w', encoding="utf-8") as f:
    for key,value in dict.items():
        st = '%s\t%s\n' %(key,value)
        f.write(unicode(st, 'utf-8'))
