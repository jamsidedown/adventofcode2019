import unittest
from part_02 import match


class Part02Tests(unittest.TestCase):

    def test_112233_passes(self):
        self.assertTrue(match(str(112233)))

    def test_123444_fails(self):
        self.assertFalse(match(str(123444)))

    def test_111122_passes(self):
        self.assertTrue(match(str(111122)))
