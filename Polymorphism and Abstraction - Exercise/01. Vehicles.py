from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: float, fuel_consumption: float) -> None:
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self):
        return None

    @abstractmethod
    def refuel(self):
        return None


class Car(Vehicle):
    ADDITIONAL_FUEL_AIR_CONSUMPTION: float = 0.9

    def drive(self, distance: float) -> float or None:
        if self.fuel_quantity >= distance * (self.fuel_consumption + Car.ADDITIONAL_FUEL_AIR_CONSUMPTION):
            self.fuel_quantity -= distance * (self.fuel_consumption + Car.ADDITIONAL_FUEL_AIR_CONSUMPTION)
            return self.fuel_quantity


    def refuel(self, fuel) -> float:
        self.fuel_quantity += fuel
        return self.fuel_quantity


class Truck(Vehicle):
    ADDITIONAL_FUEL_AIR_CONSUMPTION: float = 1.6
    TANK_PERCENTAGE_FILL = 0.95

    def drive(self, distance: float) -> float or None:
        if self.fuel_quantity >= distance * (self.fuel_consumption + Truck.ADDITIONAL_FUEL_AIR_CONSUMPTION):
            self.fuel_quantity -= distance * (self.fuel_consumption + Truck.ADDITIONAL_FUEL_AIR_CONSUMPTION)
            return self.fuel_quantity

    def refuel(self, fuel) -> float:
        self.fuel_quantity += fuel * Truck.TANK_PERCENTAGE_FILL
        return self.fuel_quantity


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
