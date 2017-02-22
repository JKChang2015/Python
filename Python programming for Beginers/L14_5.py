# L14_5
# Created by JKChang
# 22/02/2017, 10:49
# Description: 

class Hotdog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = 'raw'
        self.condiments = []

    def __str__(self):
        msg = 'hot dog'
        if len(self.condiments) > 0:
            msg = msg + ' with '
        for i in self.condiments:
            msg = msg + i + ', '
        msg = msg.strip(', ')
        msg = self.cooked_string + ' ' + msg + ' .'
        return msg

    def cook(self, time):
        self.cooked_level = self.cooked_level + time
        if self.cooked_level > 8:
            self.cooked_string = 'charcoal'
        elif self.cooked_level > 5:
            self.cooked_string = 'well-done'
        elif self.cooked_level > 3:
            self.cooked_string = 'medium'
        else:
            self.cooked_string = 'raw'


myDog = Hotdog()
print myDog

myDog.cook(4)
print myDog
