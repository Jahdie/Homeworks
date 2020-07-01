# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго
# (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться
# только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный
# метод.Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.


from time import sleep
from colorama import Back, Fore


class TrafficLight:
    __color = ""

    def __init__(self, red_seconds=7, yellow_seconds=2, green_seconds=7):
        self.green_seconds = green_seconds
        self.yellow_seconds = yellow_seconds
        self.red_seconds = red_seconds

    def running(self):
        loops = int(input("Введите количество повторений цикла светофора: "))
        for loop in range(loops):
            for red_second in range(1, int(self.red_seconds) + 1):
                TrafficLight.__color = "Red"
                print(f"\r{Back.RED} {Fore.LIGHTBLACK_EX + TrafficLight.__color} ", end="", flush=True)
                sleep(1)
            for yellow_second in range(1, int(self.yellow_seconds) + 1):
                TrafficLight.__color = "Yellow"
                print(f"\r{Back.YELLOW} {TrafficLight.__color} ", end="", flush=True)
                sleep(1)
            for green_second in range(1, int(self.green_seconds) + 1):
                TrafficLight.__color = "Green"
                print(f"\r{Back.GREEN} {TrafficLight.__color} ", end="", flush=True)
                sleep(1)
            for yellow_second in range(1, int(self.yellow_seconds) + 1):
                TrafficLight.__color = "Yellow"
                print(f"\r{Back.YELLOW} {TrafficLight.__color} ", end="", flush=True)
                sleep(1)



my_traffic_light = TrafficLight()
my_traffic_light.running()
