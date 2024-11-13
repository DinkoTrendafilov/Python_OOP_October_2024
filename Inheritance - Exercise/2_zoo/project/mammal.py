from project.animal import Animal


class Mammal(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
