import unittest
from human import Human


class TestHuman(unittest.TestCase):

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
        self.assertEqual(human_jarutas.age, 1)

    def test_reproduce(self) -> None:
        # energy is below 20 and reproduce more than required
        human_jarutas = Human("Jarutas", energy=10)
        self.assertFalse(human_jarutas.reproduce())
        # energy is below 100 and reproduce
        human_jarutas = Human("Jarutas", energy=80)
        self.assertTrue(human_jarutas.reproduce())


if __name__ == '__main__':
    unittest.main()
