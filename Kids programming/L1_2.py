import random

secret = random.randint(1,99)
guess = 0
tries = 0

print "It's a number between 1 and 99, I will give you 6 tries"

while guess != secret and tries < 6:
    guess = input('what is your guess? ')
    if  guess < secret:
        print "too low"
    elif guess > secret:
        print "too high"
    tries += 1

if guess == secret:
    print "you got it"
else:
    print "finished"


