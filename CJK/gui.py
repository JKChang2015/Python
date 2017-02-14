import easygui

flavour = easygui.enterbox('what is your favourite ice cream flavour? ')
easygui.msgbox('you entered ' + flavour)

#-------------------------------------------------------------------------
flavour = easygui.choicebox('what is your favorite ice cream flavor? ',
                           choices= ['vanilla', 'chocolate', 'strawberry'])
easygui.msgbox ('you picked ' + flavour)

#-------------------------------------------------------------------------
flavour = easygui.buttonbox('what is your favorite ice cream flavor? ',
                           choices= ['vanilla', 'chocolate', 'strawberry'])
easygui.msgbox ('you picked ' + flavour)

#-------------------------------------------------------------------------
user_response = easygui.msgbox('hello world')
