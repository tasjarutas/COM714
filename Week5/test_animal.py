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


if __name__ == '__main__':
    unittest.main()
