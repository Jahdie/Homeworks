# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric_consumption(self):
        pass


class Suit(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            self.__size = 40
        elif size > 70:
            self.__size = 70
        else:
            self.__size = size

    def fabric_consumption(self):
        size_coat = (self.size / 6.5 + 0.5)
        return f"{size_coat:.2f}"


class Coat(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 140:
            self.__height = 140
        elif height > 200:
            self.__height = 200
        else:
            self.__height = height

    def fabric_consumption(self):
        height_suit = (2 * self.height + 0.3)
        return f"{height_suit:.2f}"


my_coat = Coat(220)
my_suit = Suit(90)
print(my_suit.size)
print(my_coat.height)
print(my_coat.fabric_consumption())
print(my_suit.fabric_consumption())
