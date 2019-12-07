from collections import deque
import unittest
from part_01 import run_thrusters


class Part01Tests(unittest.TestCase):

    def test_first_example(self):
        program = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'.split(',')
        phase_settings = deque([4, 3, 2, 1, 0])
        result = run_thrusters(program, phase_settings)
        self.assertEqual(result, 43210)

    def test_second_example(self):
        program = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'.split(',')
        phase_settings = deque([0, 1, 2, 3, 4])
        result = run_thrusters(program, phase_settings)
        self.assertEqual(result, 54321)

    def test_third_example(self):
        program = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'.split(',')
        phase_settings = deque([1, 0, 4, 3, 2])
        result = run_thrusters(program, phase_settings)
        self.assertEqual(result, 65210)
