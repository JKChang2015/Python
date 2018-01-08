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
print('\n---')


def make_shirt(message, size='m'):
    print('size of the shirt is: ' + size)
    print('content: ' + message.upper())
    print()


make_shirt(size='L', message='Rock & Roll')
make_shirt('Rolling in the deep')
make_shirt('Do me a favour', 'XL')

# ----------------- 8-5 ---------------
print('\n---')


def describe_city(city, country="UK"):
    print(city + " is in " + country)


describe_city('Manchester')
describe_city("London")
describe_city('Berlin', "Germany")
describe_city(city='Paris', country='France')

# ----------------- 8-5 ---------------
print('\n---')


def make_album(artist_name, album_name, num_songs=0):
    dict = {'artist_name': artist_name, 'album_name': album_name}
    if num_songs != 0:
        dict['num_songs'] = num_songs
    return dict


print(make_album('Adele', 'Rolling in the deep'))
print(make_album('Taylor Swift', 'Call me', 10))

# -------------------------------------------------
print('\n---')


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# -----------------8-12 Sandwiches--------------------------------
print('\n---')


def make_sandwiches(*something):
    print('making a sandwiches contains: ')
    for veg in something:
        print('-' + veg)

    print('done.....')


make_sandwiches('tomatos', 'cucumbers', 'onions', 'egss')

# -----------------8-13 personal introduction--------------------------------
print('\n---')


def build_profile(first_name, last_name, **intro):
    print('Hi my name is:', last_name, first_name)
    for key, value in intro.items():
        print('-', key + ':' + value)


build_profile(first_name='David', last_name='Ch', language='Python & Java', hobby='wood working', age='16')
