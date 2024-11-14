from project.animal import Animal


class Lion(Animal):
    LION_NEED = 50

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, Lion.LION_NEED)
