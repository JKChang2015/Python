# -*- coding: UTF-8 -*-
# Q042
# Created by JKChang
# Wed, 31/05/2017, 15:34
# Tag: bits of OS
# Description: Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS. 

# For 32 bit it will return 32 and for 64 bit it will return 64

import platform
import struct

print(struct.calcsize("P") * 8)

print(platform.architecture()[0])
