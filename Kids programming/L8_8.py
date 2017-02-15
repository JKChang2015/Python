
someinput = raw_input('pls input a number between 0 to 10: ')

while (int(someinput) >= 0 and int(someinput) <= 10):
    print 'thank you for your input, your input is legal \n'
    print 'please input a numer between 0 to 10'
    someinput = raw_input()
print 'Sorry, your input is out of range, quite the program'
