# enum_test
# Created by JKChang
# 17/08/2017, 16:17
# Tag:
# Description: 

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
print(Color.RED.value)