from project.animal import Animal


class Tiger(Animal):
    TIGER_NEED = 45

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, Tiger.TIGER_NEED)
