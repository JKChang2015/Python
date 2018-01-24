# die
# Created by JKChang
# 22/01/2018, 14:41
# Tag:
# Description: 

from random import randint


class Die():

    def __init__(self, num_size=6):
        self.num_sies = num_size

    def roll(self):
        return randint(1, self.num_sies)
