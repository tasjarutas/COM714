import unittest

from human import Human
from planet import Planet


class TestPlanet(unittest.TestCase):

    def test_add_human(self):
        # check: 0 population
        earth = Planet("Earth")
        self.assertEqual(earth.population(), 0, "Population should be 0.")

        # check: single human
        jarutas = Human("Jarutas")
        earth.add(jarutas)
        self.assertEqual(earth.population(), 1, "Population should be 1.")

    def test_has(self):
        # check: does not have specified human
        earth = Planet("Earth")
        jarutas = Human("Jarutas")
        self.assertFalse(earth.has(jarutas), "Should be false.")

        # check: has specified human
        earth.add(jarutas)
        self.assertTrue(earth.has(jarutas), "Should be true.")

    def test_population(self):
        # check: no population
        earth = Planet("Earth")
        self.assertEqual(earth.population(), 0, "Population should be 0.")

        # check: no population of one
        jarutas = Human("Jarutas")
        earth.add(jarutas)
        self.assertEqual(earth.population(), 1, "Population should be 1")


if __name__ == '__main__':
    unittest.main()
