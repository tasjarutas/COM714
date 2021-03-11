import unittest
from clothing import Clothing
from clothing_size import ClothingSize

class TestClothing(unittest.TestCase):

    def test_create_clothing(self):
        size = ClothingSize.SMALL
        shirt = Clothing("red", "cotton", size)
        expect = "Clothing(colour = red, material = cotton,size=small)"
        #self.assertEqual(shirt.colour, "red", "Red Cloth is created")
        #self.assertEqual(shirt.material, "cotton", "Cotton Cloth is created")
        #self.assertEqual(shirt.size, "small", "Small size cloth")
        self.assertEqual(expect,repr(Clothing),"Clothing does not match")

if __name__ == '__main__':
    unittest.main()
