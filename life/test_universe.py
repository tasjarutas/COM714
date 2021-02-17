import unittest

from human import Human
from planet import Planet
from universe import Universe


class TestUniverse(unittest.TestCase):

    def test_generate(self):
        # check: no planet
        start = Universe()
        self.assertEqual(start.universe_size(), 0, "Universe should be 0.")

        # check: single planet
        earth = Planet("Earth")
        start = Universe()
        start.generate(earth)
        self.assertEqual(start.universe_size(), 1, "Universe should be 1.")

    def test_display(self):
        # check: no planet
        start = Universe()
        self.assertEqual(start.display(), None, "Universe should be none.")

        # check: one planet
        earth = Planet("Earth")
        start = Universe()
        start.generate(earth)
        self.assertEqual(start.display(), None, "Universe has earth")


if __name__ == '__main__':
    unittest.main()
