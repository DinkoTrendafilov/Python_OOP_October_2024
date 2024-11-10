from typing import List


class Vehicle:
    def __init__(self, mileage: float, max_speed: int = 150) -> None:
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets: List[str] = []


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
