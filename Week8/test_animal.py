import unittest
from animal import Animal


class TestAnimal(unittest.TestCase):

    def test_grow(self):
        animal = Animal("Cat")
        animal.grow()
        self.assertEqual(animal.get_age(), 1, "Animal is growing")

    def test_reproduce(self):
        # energy is below 1 and reproduce more than required
        animal = Animal("Cat", energy=0)
        self.assertFalse(animal.reproduce())
        # energy is 100 and reproduce
        animal = Animal("Cat", energy=100)
        self.assertTrue(animal.reproduce())

    def test_move(self):
        # Try to move when energy is less than moving enery
        animal = Animal("Cat", energy=5)
        self.assertFalse(animal.move(5))
        # Try to move when enery is enough
        animal = Animal("Cat", energy=50)
        self.assertTrue(animal.move(10))

    def test_eat(self):
        # Try to eat when the energy is full
        animal = Animal("Cat", energy=100)
        self.assertEqual(animal.eat(20), 20, "Energy excess should be 20.")

        # Try to eat when the energy below full
        animal = Animal("Cat", energy=80)
        self.assertEqual(animal.eat(20), 0, "Energy is at the maximum as 100.")

        # Try to eat while still have room for eating
        animal = Animal("Cat", energy=50)
        self.assertEqual(animal.eat(20), -30, "Excess should be -30")


if __name__ == '__main__':
    unittest.main()
