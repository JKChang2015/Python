# L14_5
# Created by JKChang
# 22/02/2017, 10:49
# Description: 

class Hotdog:
    def __init__(self):
        self.cooked_level = 0
        self.cooked_string = 'Raw'
        self.condiments = []

    def __str__(self):
        msg = 'hot dog'
        if len(self.condiments) > 0:
            msg = msg + ' with '
        for i in self.condiments:
            msg = msg + i + ', '
        msg = msg.strip(', ')
        msg = self.cooked_string + ' ' + msg + '.'
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

    def addCondiment(self, condiment):
        self.condiments.append(condiment)

myDog = Hotdog()
print myDog

print '\ncooking hot for 4 minutes'
myDog.cook(4)
print myDog

print '\ncooking hot for 3 more minutes'
myDog.cook(3)
print myDog

print '\nNow, adding some stuff on my hot dog'
myDog.addCondiment('ketchup')
myDog.addCondiment('Mustard')
print myDog
