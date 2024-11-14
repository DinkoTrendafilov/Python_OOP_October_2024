from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: list[Animal] = []
        self.workers: list[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"

        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        fire_worker = next((worker for worker in self.workers if worker.name == worker_name), None)
        if fire_worker:
            self.workers.remove(fire_worker)
            return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        money_to_pay = sum([w.salary for w in self.workers])
        if money_to_pay <= self.__budget:
            self.__budget -= money_to_pay
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        money_to_feed_animals = sum([a.money_for_care for a in self.animals])
        if money_to_feed_animals <= self.__budget:
            self.__budget -= money_to_feed_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals\n"
        lions = [l for l in self.animals if l.__class__.__name__ == "Lion"]
        tigers = [t for t in self.animals if t.__class__.__name__ == "Tiger"]
        cheetahs = [c for c in self.animals if c.__class__.__name__ == "Cheetah"]
        amount_of_lions = len(lions)
        amount_of_tigers = len(tigers)
        amount_of_cheetahs = len(cheetahs)

        result += f"----- {amount_of_lions} Lions:\n"
        for lion in lions:
            result += f"{lion}\n"

        result += f"----- {amount_of_tigers} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger}\n"

        result += f"----- {amount_of_cheetahs} Cheetahs:\n"
        for cheet in cheetahs:
            result += f"{cheet}\n"

        return result.strip()

    def workers_status(self) -> str:
        result = f"You have {len(self.workers)} workers\n"
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [kt for kt in self.workers if kt.__class__.__name__ == "Caretaker"]
        vetes = [v for v in self.workers if v.__class__.__name__ == "Vet"]
        amount_of_keepers = len(keepers)
        amount_of_caretakers = len(caretakers)
        amount_of_vetes = len(vetes)

        result += f"----- {amount_of_keepers} Keepers:\n"
        for keeper in keepers:
            result += f"{keeper}\n"

        result += f"----- {amount_of_caretakers} Caretakers:\n"
        for caretaker in caretakers:
            result += f"{caretaker}\n"

        result += f"----- {amount_of_vetes} Vets:\n"
        for vet in vetes:
            result += f"{vet}\n"

        return result.strip()
