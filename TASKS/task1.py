class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age


p = Person('Sanya', 'Volkov', 17)
print(p.get_name())
print(p.get_surname())
print(p.age)

p.age = 18
print(p.age)