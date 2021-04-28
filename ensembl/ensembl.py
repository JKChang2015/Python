# -*- coding: UTF-8 -*-
# File name: ensembl
# Created by JKChang
# 05/04/2021, 17:13
# Tag:
# Description:

import vcf
vcf_reader = vcf.Reader(filename=r'./CEU.exon.2010_09.genotypes.vcf.gz')
for record in vcf_reader:
    print(record.ID,record.INFO,record.POS,record.aaf)

