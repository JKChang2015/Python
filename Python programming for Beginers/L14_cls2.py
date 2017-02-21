# L14_cls2
# Created by JKChang
# 21/02/2017, 15:21
# Description: __init()__

class Ball:
    'I have something to say'

    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def bounce(self):
        if self.direction == 'down':
            self.direction = 'up'


myBall = Ball('red', 'small', 'down')
# print attributes
print 'I just creat a ball.'
print 'Size of the ball is ', myBall.size
print 'Color of the ball is ', myBall.color
print 'Direction', myBall.direction
print 'Now I will bounce the ball'
print

# Method
myBall.bounce()
print 'now the direction is: ', myBall.direction
print
