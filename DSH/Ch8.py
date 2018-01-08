# Ch8
# Created by JKChang
# 08/01/2018, 10:59
# Tag:
# Description: Function

# ----------------- 8-1 ---------------
def display_message(message):
    print(message)


display_message('Hi, print from a function')
display_message('This is second line of the message')

# ----------------- 8-3 /4 ---------------
print('---')


def make_shirt(message, size='m'):
    print('size of the shirt is: ' + size)
    print('content: ' + message.upper())
    print()


make_shirt(size='L', message='Rock & Roll')
make_shirt('Rolling in the deep')
make_shirt('Do me a favour', 'XL')

# ----------------- 8-5 ---------------
print('---')


def describe_city(city, country="UK"):
    print(city + " is in " + country)


describe_city('Manchester')
describe_city("London")
describe_city('Berlin', "Germany")
describe_city(city='Paris', country='France')

# ----------------- 8-5 ---------------
print('---')


def make_album(artist_name, album_name, num_songs=0):
    dict = {'artist_name': artist_name, 'album_name': album_name}
    if num_songs != 0:
        dict['num_songs'] = num_songs
    return dict


print(make_album('Adele', 'Rolling in the deep'))
print(make_album('Taylor Swift', 'Call me', 10))
