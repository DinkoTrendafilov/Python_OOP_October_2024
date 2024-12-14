class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):
    def test_init_cat(self):
        cat = Cat('Fluffy')
        self.assertEqual(cat.name, 'Fluffy')
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(cat.size, 0)

    def test_cat_increase_size(self):
        cat = Cat('Fluffy')
        cat.eat()
        self.assertTrue(cat.fed)
        self.assertTrue(cat.sleepy)
        self.assertEqual(cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        cat = Cat('Fluffy')
        cat.eat()
        self.assertTrue(cat.fed)
        with self.assertRaises(Exception):
            cat.eat()

    def test_cat_can_not_eat_already_fed(self):
        cat = Cat('Fluffy')
        cat.eat()
        with self.assertRaises(Exception):
            cat.sleep()

    def test_cat_can_not_asleep_is_not_fed(self):
        cat = Cat('Fluffy')
        with self.assertRaises(Exception):
            cat.sleep()

    def test_cat_not_sleepy_after_sleeping(self):
        cat = Cat('Fluffy')
        cat.eat()
        cat.sleep()
        self.assertFalse(cat.sleepy)

        with self.assertRaises(Exception):
            cat.sleep()


if __name__ == "__main__":
    main()
