import unittest
from part_02 import passes_criteria


class Part02Tests(unittest.TestCase):

    def test_112233_passes(self):
        passes = passes_criteria(112233)
        self.assertTrue(passes)

    def test_123444_fails(self):
        passes = passes_criteria(123444)
        self.assertFalse(passes)

    def test_111122_passes(self):
        passes = passes_criteria(111122)
        self.assertTrue(passes)
