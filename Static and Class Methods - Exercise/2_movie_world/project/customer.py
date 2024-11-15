from project.dvd import DVD


class Customer:
    def __init__(self, name: str, age: int, _id: int):
        self.name = name
        self.age = age
        self.id = _id
        self.rented_dvds: list[DVD] = []

    def __repr__(self) -> str:
        return (f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} "
                f"rented DVD's ({', '.join(x.name for x in self.rented_dvds)})")
