from task_3_box import box


class Truck:
    def __init__(self, capacity):
        self.__capacity = capacity

    def __str__(self):
        return f'Емкость грузовика: {len(self.__capacity)} посылок'

    def add(self, box):
        self.__capacity.append(box)

    def sub(self, box):
        self.__capacity.remove(box)


truck = Truck([])
box1 = box('box1', 'Москва', 'Казань')
box2 = box('box2', 'Казань', 'Москва')

truck.add(box1)
truck.add(box2)

print(truck)
truck.sub(box1)
print(truck)