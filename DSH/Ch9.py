# Ch9
# Created by JKChang
# 08/01/2018, 16:16
# Tag:
# Description: Classes
# —————————————— 9-1 / 4 ----------------------

class Restaurant():
    ''''a class of restaurant'''

    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + ' is a ' + self.cuisine_type + ' restaurant')

    def open_restaurant(self):
        print(self.restaurant_name + ' is opening')

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num


r1 = Restaurant('Hola', "Chinese food")
r2 = Restaurant('Soho', "USA burger")
r3 = Restaurant('Soul plaza', "Korea food")

r1.describe_restaurant()
r2.describe_restaurant()
r3.describe_restaurant()

r1.open_restaurant()
r2.open_restaurant()
r3.open_restaurant()

# -----------------Inheritance-----------------------
print('----------------')


class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        longname = str(self.year) + ' ' + self.make + ' ' + self.model
        return longname

    def read_odometer(self):
        print('this car has ' + str(self.odometer_reading) + 'miles on it.')

    def update_odometer(self, num):
        if num > self.odometer_reading:
            self.odometer_reading = num
        else:
            print('You can roll back the odometer')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def gas_tank(self):
        print('fill the gas tank')


class ElectricCar(Car):
    def __init__(self, make, model, year, power):
        super().__init__(make, model, year)
        self.power = power

    def get_description(self):
        c = super().get_description()
        return c + 'battery = ' + str(self.power)

    def gas_tank(self):
        print("this car doesn't need gas.")


t1 = ElectricCar(year=2016, model='X', make='Tesla', power=1999)
print(t1.get_description())
t1.gas_tank()
