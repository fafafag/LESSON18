import random


class Box:
    def __init__(self, name, from_city, target_city):
        self.__postcode = random.randint(1000000, 9999999)
        self.__name = name
        self.__from_city = from_city
        self.__target_city = target_city

    def get_postcode(self):
        return self.__postcode

    def get_name(self):
        return self.__name

    def get_from_city(self):
        return self.__from_city

    def get_target_city(self):
        return self.__target_city

    def set_target_city(self, new_target_city):
        self.__target_city = new_target_city


box1 = Box('Юлия', 'Москва', 'Казань')
print(box1.get_postcode())
print(box1.get_name())
print(box1.get_from_city())
print(box1.get_target_city())
box1.set_target_city('Белгород')
print(box1.get_target_city())