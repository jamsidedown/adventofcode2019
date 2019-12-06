import unittest
from part_01 import run


class Part01Tests(unittest.TestCase):

    def test_example_returns_42(self):
        orbits = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
        total_orbits = run(orbits)
        self.assertEqual(total_orbits, 42)
