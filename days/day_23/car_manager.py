import random
from car import Car


def make_car():
    new_car = Car()
    super_car_chance = random.randint(1, 10)
    new_car.is_super_car = super_car_chance == 6
    return new_car


class CarManager:

    def __init__(self):
        self.cars = []
        self.maximum_car_production = 3

    def create_cars(self):
        for _ in range(random.randint(1, self.maximum_car_production)):
            new_car = make_car()
            self.cars.append(new_car)
