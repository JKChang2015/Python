# Ch7
# Created by JKChang
# 07/01/2018, 18:10
# Tag:
# Description: input and while

# -------------------input -----------------------------------------------
name = input("what's your name please?  ")
message = input('please leave your messages:  ')
print('hi, David you have one message come from', name,
      '\n"', message, '"')

# --------------------while & List/Dict -----------------------------------
print()
unconfirmed_user = ['Alice','brain','Gareth']
confirmed = []

while unconfirmed_user:
      curr_user = unconfirmed_user.pop()
      print('verifying user: ' + curr_user.title())
      confirmed.append(curr_user.title())

print('\nthe following users have been confirmed: ')
for user in confirmed:
      print(user)

# --------------------while remove()-----------------------------------
print()
pets = ['cat','dog','bird','cat','cat']
print(pets)
while 'cat' in pets:
      pets.remove('cat')

print('after remove cat:', pets)
