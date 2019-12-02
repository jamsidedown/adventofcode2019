import unittest
from part_01 import run


class Part01Tests(unittest.TestCase):

    def test_example_case(self):
        example_text = '1,9,10,3,2,3,11,0,99,30,40,50'
        program = [int(op) for op in example_text.split(',')]
        result = run(program)
        self.assertEqual(result, 3500)
