# Ch6
# Created by JKChang
# 07/01/2018, 16:07
# Tag:
# Description: dict

favorite_num = {
    'Mike': 7,
    'David': 14,
    'Claire': 4,
    'John': 34,
    'Lee': 1
}

# print("Claire's favourite number is: " + str(favorite_num['Claire']))

for key, value in favorite_num.items():
    print(key + "'s favourite number is: " + str(value))

print()

for key, value in sorted(favorite_num.items()):
    print(key + "'s favourite number is: " + str(value))

# -----------------------6-7--------------------------------
p1 = {'first_name': 'Mike', 'last_name': 'White', 'age': 18, 'city': 'Manchester'}
p2 = {'first_name': 'Claire', 'last_name': 'Smith', 'age': 41, 'city': 'Cambridge'}
p3 = {'first_name': 'Mike', 'Taylor': 'Swift', 'age': 32, 'city': 'London'}
people = [p1, p2, p3]

for p in people:
    for key, value in p.items():
        print(key + ": " + str(value))
    print()

# -----------------------6-8--------------------------------
pet1 = {'type': 'dog', 'owner': 'Zoe'}
pet2 = {'type': 'cat', 'owner': 'Gareth'}
pet3 = {'type': 'bird', 'owner': 'Chandu'}
pets = [pet1, pet2, pet3]

for pet in pets:
    for key, value in pet.items():
        print(key + ": " + value)
    print()
