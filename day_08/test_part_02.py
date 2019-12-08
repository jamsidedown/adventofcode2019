import unittest
from part_01 import get_layers
from part_02 import flatten


class Part02Tests(unittest.TestCase):

    def test_example(self):
        image = [int(x) for x in '0222112222120000']
        layers = get_layers(image, 2, 2)
        flattened = flatten(layers)
        expected = [[0, 1], [1, 0]]
        self.assertListEqual(flattened, expected)
