# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
from random import choice, randint


# list_direction = ["налево", "направо", "вперед", "назад"]
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.move = choice([True, False])
        self.direction = choice(["налево", "направо", "вперед", "назад"])

    def go(self):
        if self.move is True:
            return "едет,"
        else:
            return ""

    def stop(self):
        if self.move is False:
            return "стоит,"
        else:
            return ""

    def turn(self, drection):
        self.direction = drection
        if self.move:
            return f"машина движется {self.direction}"
        else:
            print(f"машина пока не имеет направления движения")

    def show_speed(self):
        if self.move is True:
            return self.speed
        else:
            return "отсутвствует"

    def status(self):
        status_text = f"Машина {self.color} {self.name} " \
                  f"{self.go()}{self.stop()}" \
                  f" скорость {self.show_speed()}," \
                  f" направление движения {self.direction if self.move is True else 'отсутствует'}," \
                  f" это {'полицейская' if self.is_police else 'гражданская'} машина."
        return print(status_text)


class TownCar(Car):
    def show_speed(self):
        if self.move is True and self.speed > 40:
            return "превышена"
        else:
            return "отсутствует"


class WorkCar(Car):
    def show_speed(self):
        if self.move is True and self.speed > 40:
            return "превышена"
        else:
            return "отсутствует"


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


my_town_car = TownCar(randint(20, 65), "Red", "Niva", False)
my_town_car_2 = TownCar(randint(20, 65), "Blue", "Lada", False)
my_sport_car = SportCar(randint(100, 200), "Black", "Ferrari", False)
my_work_car = WorkCar(randint(10, 45), "Yellow", "Liaz", False)
my_work_car_2 = WorkCar(randint(10, 45), "White", "Gaz", False)
my_police_car = PoliceCar(randint(50, 120), "Green", "Uaz", True)

my_town_car.status()
my_town_car_2.status()
my_sport_car.status()
my_work_car.status()
my_work_car_2.status()
my_police_car.status()
