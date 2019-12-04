import unittest
from part_01 import match


class Part01Tests(unittest.TestCase):

    def test_111111_passes(self):
        self.assertTrue(match(str(111111)))

    def test_223450_fails(self):
        self.assertFalse(match(str(223450)))

    def test_123789_fails(self):
        self.assertFalse(match(str(123789)))
