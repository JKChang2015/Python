import random
import easygui

secret = random.randint(1,99)
guess = 0
tries = 0

easygui.msgbox ("Hi, pls guess a number from 1 to 99. I will give you 8 tries")

while guess != secret and tries < 8:
    guess = easygui.integerbox("what is your guess? ")
    if not guess: break

    if guess < secret:
        easygui.msgbox(str(guess) + " is too low")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high")
    tries += 1

if guess == secret:
    easygui.msgbox ('you got it')
else:
    easygui.msgbox(" you loose ")