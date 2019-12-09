import unittest
from unittest.mock import call, patch
from part_01 import IntcodeComputer


class Part01Tests(unittest.TestCase):

    @patch('builtins.print')
    def test_first_example(self, mock_print):
        program = '109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99'.split(',')
        computer = IntcodeComputer(program)
        computer.run(0)
        calls = [call(int(x)) for x in program]
        mock_print.assert_has_calls(calls)

    @patch('builtins.print')
    def test_second_example(self, mock_print):
        program = '1102,34915192,34915192,7,4,7,99,0'.split(',')
        computer = IntcodeComputer(program)
        computer.run(0)
        mock_print.assert_called_once_with(1219070632396864)

    @patch('builtins.print')
    def test_third_example(self, mock_print):
        program = '104,1125899906842624,99'.split(',')
        computer = IntcodeComputer(program)
        computer.run(0)
        mock_print.assert_called_once_with(1125899906842624)
