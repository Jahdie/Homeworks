# Реализовать класс Stationery(канцелярская принадлежность).Определить в нем атрибут title(название) и метод
# draw(отрисовка).Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen(ручка), Pencil(карандаш), Handle(маркер).В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводитьуникальное сообщение.Создать экземпляры классов и проверить,
# что выведет описанный  метод  для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Выбрана ручка {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Выбран карандаш {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Выбран маркер {self.title}")


my_stationery = Stationery("канцелярских предметов:")
my_pen = Pen("шариковая, черного цвета.")
my_pencil = Pencil("твердый, для тонких линий.")
my_handle = Handle("перманентный, для линий 4 мм.")

my_stationery.draw()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
