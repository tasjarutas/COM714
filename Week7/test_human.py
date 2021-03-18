import unittest
from human import Human
from clothing_size import ClothingSize
from clothing import Clothing


class TestHuman(unittest.TestCase):

    def test_dress(self) -> None:
        human_jarutas = Human("Jarutas")
        shirt = Clothing("blue", "cotton", ClothingSize.MEDIUM)
        human_jarutas.dress(shirt)
        self.assertEqual(human_jarutas.number_dress(), 1, "Number of clothing is 1")

    def test_undress(self) -> None:
        human_jarutas = Human("Jarutas")
        shirt = Clothing("blue", "cotton", ClothingSize.MEDIUM)
        human_jarutas.dress(shirt)
        human_jarutas.undress(shirt)
        self.assertEqual(human_jarutas.number_dress(), 0, "Number of clothing is 0")


    def test_eat(self) -> None:
        # energy is full and try to eat
        human_jarutas = Human("Jarutas")
        self.assertEqual(human_jarutas.eat(20), 20, "Excess should be 20.")

        # energy is below 100 and eat more than required
        human_jarutas = Human("Jarutas", energy=90)
        self.assertEqual(human_jarutas.eat(20), 10, "Excess should 20.")

        # energy is below 100 and eat exactly what is required
        human_jarutas = Human("Jarutas", energy=80)
        self.assertEqual(human_jarutas.eat(20), 0, "Excess should be 0.")

        # energy is below 100 and eat less than required
        human_jarutas = Human("Jarutas", energy=70)
        self.assertEqual(human_jarutas.eat(20), -10, "Excess should be -10.")

    # Add additional tests here.
    def test_grow(self) -> None:
        # growing
        human_jarutas = Human("Jarutas")
        human_jarutas.grow()
        self.assertEqual(human_jarutas._age, 1, "Human_jarutas grows")

    def test_reproduce(self) -> None:
        # energy is below 20 and reproduce more than required
        human_jarutas = Human("Jarutas", energy=10)
        self.assertFalse(human_jarutas.reproduce())
        # energy is below 100 and reproduce
        human_jarutas = Human("Jarutas", energy=80)
        self.assertTrue(human_jarutas.reproduce())


if __name__ == '__main__':
    unittest.main()
