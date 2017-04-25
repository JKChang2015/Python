import random

# 25April
# Created by JKChang
# 25/04/2017, 09:58
# Description: reviewing

start = 1
end = 99

secret = random.randint(start, end)
guess = 0
tries = 0

print "It's a number between", start, 'and', end, ", I will give you 7 tries"

while guess != secret and tries < 7:
    guess = input('what is your guess? ')
    if guess < secret:
        print 'too low'
    elif guess > secret:
        print 'too high'
    tries += 1

if guess == secret:
    print 'You got it'
else:
    print 'finished'
