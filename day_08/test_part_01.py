import unittest
from part_01 import run


class Part01Tests(unittest.TestCase):

    def test_example(self):
        image = [int(x) for x in '123456789012']
        layers = run(image, 3, 2)
        expected = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 1, 2]]]
        self.assertListEqual(layers, expected)
