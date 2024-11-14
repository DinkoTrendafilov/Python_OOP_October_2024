from project.animal import Animal


class Cheetah(Animal):
    CHEETAH_NEED = 60

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, Cheetah.CHEETAH_NEED)
