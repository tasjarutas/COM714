import unittest

from human import Human
from planet import Planet


class TestPlanet(unittest.TestCase):

    def test_add_human(self):
        # check: 0 population
        planet = Planet("Earth")
        self.assertEqual(planet.population(), 0, "Population should be 0.")

        # check: single human
        human = Human("Jarutas")
        planet.add(human)
        self.assertEqual(planet.population(), 1, "Population should be 1.")

    def test_remove(self) -> None:
        # check1: planet with 1 person
        planet = Planet("Earth")
        human = Human("Jarutas")
        planet.add(human)
        self.assertEqual(planet.population(), 1, "Population should be 1.")
        planet.remove(human)
        self.assertEqual(planet.population(), 0, "Population should be 0.")

    def test_has(self):
        # check: does not have specified human
        planet = Planet("Earth")
        human = Human("Jarutas")
        self.assertFalse(planet.has(human), "Should be false.")

        # check: has specified human
        human = Human("Jarutas")
        planet.add(human)
        self.assertTrue(planet.has(human), "Should be true.")

    def test_population(self):
        # check: no population
        planet = Planet("Earth")
        self.assertEqual(planet.population(), 0, "Population should be 0.")

        # check: no population of one
        human = Human("Jarutas")
        planet.add(human)
        self.assertEqual(planet.population(), 1, "Population should be 1")


if __name__ == '__main__':
    unittest.main()
