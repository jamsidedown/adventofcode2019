import unittest
from part_01 import passes_criteria


class Part01Tests(unittest.TestCase):

    def test_111111_passes(self):
        passes = passes_criteria(111111)
        self.assertTrue(passes)

    def test_223450_fails(self):
        passes = passes_criteria(223450)
        self.assertFalse(passes)

    def test_123789_fails(self):
        passes = passes_criteria(123789)
        self.assertFalse(passes)
