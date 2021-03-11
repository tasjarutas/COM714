import unittest
from superhuman import SuperHuman


class TestSuperHuman(unittest.TestCase):

    def test_fly(self):
        super_tas = SuperHuman("Jarutas", energy=10)
        self.assertTrue(super_tas.fly(5))

        super_tas = SuperHuman("Jarutas", energy=5)
        self.assertFalse(super_tas.fly(5))


if __name__ == '__main__':
    unittest.main()
