# -*- coding: UTF-8 -*-
# Q044
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: locate python site-package
# Description: Write a Python program to locate Python site-packages. 
import site;

print('\n'.join(site.getsitepackages()))
