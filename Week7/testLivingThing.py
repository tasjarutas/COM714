import unittest
from livingthing import LivingThing


class TestLivingthing(unittest.TestCase):

    def test_grow(self):
        living = LivingThing("Human")
        living.grow()
        living.grow()
        living.grow()
        self.assertEqual(living._age, 3, "Age should be 3")

    def test_reproduce(self):
        # energy is below 1 and reproduce more than required
        living = LivingThing("Human", energy=0)
        self.assertFalse(living.reproduce())
        # energy is 100 and reproduce
        living = LivingThing("Human", energy=100)
        self.assertTrue(living.reproduce())


if __name__ == '__main__':
    unittest.main()
