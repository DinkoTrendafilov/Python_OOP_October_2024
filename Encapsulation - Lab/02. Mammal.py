class Mammal:
    __KINGDOM = "animals"

    def __init__(self, name: str, _type: str, sound: str) -> None:
        self.name = name
        self.type = _type
        self.sound = sound

    def make_sound(self) -> str:
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self) -> str:
        return self.__KINGDOM

    def info(self) -> str:
        return f"{self.name} is of type {self.type}"


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
