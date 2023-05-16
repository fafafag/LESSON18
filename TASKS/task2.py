from abc import ABC, abstractmethod


class Cloth(ABC):
    reserved = 0

    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def fabric_consumption(self):
        pass

    @property
    def total_fabric_consumption(self):
        return self.fabric_consumption() + self.reserved


class Coat(Cloth):
    def fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Cloth):
    def fabric_consumption(self):
        return 2 * self.size + 0.3

    # пример использования классов


coat = Coat("Пальто", 100)
suit = Suit("Костюм", 178)

print(coat.name, coat.size, coat.total_fabric_consumption)
print(suit.name, suit.size, suit.total_fabric_consumption)

total_fabric_consumption = coat.total_fabric_consumption + suit.total_fabric_consumption
print("Расход ткани:", total_fabric_consumption)