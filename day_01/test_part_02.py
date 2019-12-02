import unittest
from part_02 import run


class Part02Tests(unittest.TestCase):

    def test_mass_of_14(self):
        fuel = run([14])
        self.assertEqual(fuel, 2)

    def test_mass_of_1969(self):
        fuel = run([1969])
        self.assertEqual(fuel, 966)

    def test_mass_of_100756(self):
        fuel = run([100756])
        self.assertEqual(fuel, 50346)
