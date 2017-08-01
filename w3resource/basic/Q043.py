# -*- coding: UTF-8 -*-
# Q043
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: platform information
# Description: Write a Python program to get OS name, platform and release information. 
import os
import platform

print(os.name)
print(platform.system())
print(platform.release())
print(platform.version())

