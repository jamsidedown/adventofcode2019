import unittest
from part_02 import run


class Part02Tests(unittest.TestCase):

    def test_example(self):
        orbits = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']
        jumps = run(orbits)
        self.assertEqual(jumps, 4)
