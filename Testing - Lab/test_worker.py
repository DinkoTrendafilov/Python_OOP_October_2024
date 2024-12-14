class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'




from unittest import TestCase, main
class WorkerTests(TestCase):
    def test_init_worker(self):
        w = Worker("Test", 1000, 100)

        self.assertEqual(w.name, "Test")
        self.assertEqual(w.salary, 1000)
        self.assertEqual(w.energy, 100)
        self.assertEqual(w.money, 0)

    def test_work_worker_does_not_have_energy_raises(self):
        w = Worker("Test", 1000, 0)

        self.assertEqual(w.salary, 1000)
        self.assertEqual(w.energy, 0)

        with self.assertRaises(Exception) as ex:
            w.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

        self.assertEqual(w.salary, 1000)
        self.assertEqual(w.energy, 0)

        w = Worker("Test", 1000, -10)
        self.assertEqual(w.salary, 1000)
        self.assertEqual(w.energy, -10)

        with self.assertRaises(Exception) as ex:
            w.work()

        self.assertEqual("Not enough energy.", str(ex.exception))
        self.assertEqual(w.salary, 1000)
        self.assertEqual(w.energy, -10)

    def test_work_worker_works(self):
        w = Worker("Test", 1000, 100)

        self.assertEqual(w.salary, 1000)
        self.assertEqual(w.energy, 100)

        w.work()

        self.assertEqual(w.money, 1000)
        self.assertEqual(w.energy, 99)

        w.work()

        self.assertEqual(w.money, 2000)
        self.assertEqual(w.energy, 98)

    def test_rest_worker_energy_increases(self):
        w = Worker("Test", 1000, 100)

        self.assertEqual(w.energy, 100)

        w.rest()

        self.assertEqual(w.energy, 101)

    def test_get_info(self):
        w = Worker("Test", 1000, 100)

        self.assertEqual(w.get_info(), "Test has saved 0 money.")

        w.work()
        w.work()

        self.assertEqual(w.get_info(), "Test has saved 2000 money.")


if __name__ == "__main__":
    main()
