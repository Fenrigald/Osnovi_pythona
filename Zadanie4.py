class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} Car going")

    def stop(self):
        print(f"{self.name} Car stopping")

    def turn(self, direction):
        print(f"{self.name} Car turn {direction}")

    def show_speed(self):
        print(f"{self.name} speed: {self.speed}")


class TownCar(Car):
    def show_speed(self):
        return f"{self.name} speed: {self.speed}. Overspeeding" if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        return f"{self.name} speed: {self.speed}. Overspeeding" if self.speed > 40 else super().show_speed()


class SportCar(Car):
    """SportCar"""


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


wc = WorkCar(50, 'Dark', 'Cargo', False)
sc = SportCar(100, 'Red', 'Mustang', False)
pc = PoliceCar(70, 'White', 'Cap')
tc = TownCar(50, 'Grey', 'Audi', False)
lc = [wc, sc, pc, tc]
for c in lc:
    c.go()
    print(c.show_speed())
    c.turn('left')
    c.stop()