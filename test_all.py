from main.gardener import Gardener
from main.tomatoes import  BagOfTomatoes
from main.carrots import BagOfCarrots
from main.potatoes import BagOfPotatoes
from main.garden import Garden
import unittest


class test(unittest.TestCase):
    def test_Potatoes(self):
        azerty = BagOfPotatoes()
        self.assertTrue(type(azerty.seeds_number == int))
        self.assertEqual(azerty.seeds_number,0)
        azerty = BagOfPotatoes(3)
        self.assertEqual(azerty.seeds_number,3)
    
    def test_Carrots(self):
        azerty = BagOfCarrots()
        self.assertTrue(type(azerty.seeds_number == int))
        self.assertEqual(azerty.seeds_number,0)
        azerty = BagOfCarrots(3)
        self.assertEqual(azerty.seeds_number,3)

    def test_Tomatoes(self):
        azerty = BagOfTomatoes()
        self.assertTrue(type(azerty.seeds_number == int))
        self.assertAlmostEqual(azerty.seeds_number,0)
        azerty = BagOfTomatoes(3)
        self.assertEqual(azerty.seeds_number,3)

    def test_Garden(self):
        azerty = (Garden())
        self.assertTrue(type(azerty.SIZE == int))
        self.assertEqual(azerty.SIZE, 30)
        self.assertEqual(azerty.listgraines, [])
        self.assertTrue(azerty.counter()==0)

    def test_Gardener(self):
        azerty = Gardener()


if __name__ == '__main__':
    unittest.main()