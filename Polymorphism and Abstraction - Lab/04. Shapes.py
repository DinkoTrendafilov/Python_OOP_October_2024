from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        return None

    @abstractmethod
    def calculate_perimeter(self):
        return None


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.__radius = radius

    def calculate_area(self) -> float:
        return pi * self.__radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * pi * self.__radius


class Rectangle(Shape):
    def __init__(self, height: float, width: float) -> None:
        self.__height = height
        self.__width = width

    def calculate_area(self) -> float:
        return self.__height * self.__width

    def calculate_perimeter(self) -> float:
        return 2 * (self.__height + self.__width)


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
