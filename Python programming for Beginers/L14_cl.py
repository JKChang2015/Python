# L14_cl
# Created by JKChang
# 21/02/2017, 09:41
# Description: simple ball class

class Ball:
    def bounce(self):
        if self.direction == 'down':
            self.direction = 'up'

myBall = Ball()
myBall.direction = 'down'
myBall.color = "red"
myBall.size = 'small'

print 'I just creat a ball.'
print 'Size of the ball is ', myBall.size
print 'Color of the ball is ', myBall.color
print 'Direction', myBall.direction
print 'Now I will bounce the ball'
print
myBall.bounce()
print 'now the direction is: ', myBall.direction
