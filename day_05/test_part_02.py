import unittest
from unittest.mock import patch
from part_02 import run


class Part02Tests(unittest.TestCase):

    @patch('builtins.print')
    def test_first_example_true(self, mock_print):
        program = '3,9,8,9,10,9,4,9,99,-1,8'.split(',')
        run(program, '8')
        mock_print.assert_called_once_with('1')

    @patch('builtins.print')
    def test_first_example_false(self, mock_print):
        program = '3,9,8,9,10,9,4,9,99,-1,8'.split(',')
        run(program, '7')
        mock_print.assert_called_once_with('0')

    @patch('builtins.print')
    def test_second_example_true(self, mock_print):
        program = '3,9,7,9,10,9,4,9,99,-1,8'.split(',')
        run(program, '7')
        mock_print.assert_called_once_with('1')

    @patch('builtins.print')
    def test_second_example_false(self, mock_print):
        program = '3,9,7,9,10,9,4,9,99,-1,8'.split(',')
        run(program, '9')
        mock_print.assert_called_once_with('0')

    @patch('builtins.print')
    def test_third_example_true(self, mock_print):
        program = '3,3,1108,-1,8,3,4,3,99'.split(',')
        run(program, '8')
        mock_print.assert_called_once_with('1')

    @patch('builtins.print')
    def test_third_example_false(self, mock_print):
        program = '3,3,1108,-1,8,3,4,3,99'.split(',')
        run(program, '7')
        mock_print.assert_called_once_with('0')

    @patch('builtins.print')
    def test_fourth_example_true(self, mock_print):
        program = '3,3,1107,-1,8,3,4,3,99'.split(',')
        run(program, '7')
        mock_print.assert_called_once_with('1')

    @patch('builtins.print')
    def test_fourth_example_false(self, mock_print):
        program = '3,3,1107,-1,8,3,4,3,99'.split(',')
        run(program, '9')
        mock_print.assert_called_once_with('0')

    @patch('builtins.print')
    def test_fifth_example_true(self, mock_print):
        program = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'.split(',')
        run(program, '2')
        mock_print.assert_called_once_with('1')

    @patch('builtins.print')
    def test_fifth_example_false(self, mock_print):
        program = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'.split(',')
        run(program, '0')
        mock_print.assert_called_once_with('0')

    @patch('builtins.print')
    def test_sixth_example_true(self, mock_print):
        program = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'.split(',')
        run(program, '2')
        mock_print.assert_called_once_with('1')

    @patch('builtins.print')
    def test_sixth_example_false(self, mock_print):
        program = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'.split(',')
        run(program, '0')
        mock_print.assert_called_once_with('0')

    @patch('builtins.print')
    def test_seventh_example_below(self, mock_print):
        program = ('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,' +
                   '1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,' +
                   '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99').split(',')
        run(program, '7')
        mock_print.assert_called_once_with('999')

    @patch('builtins.print')
    def test_seventh_example_equal(self, mock_print):
        program = ('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,' +
                   '1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,' +
                   '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99').split(',')
        run(program, '8')
        mock_print.assert_called_once_with('1000')

    @patch('builtins.print')
    def test_seventh_example_above(self, mock_print):
        program = ('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,' +
                  '1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,' +
                  '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99').split(',')
        run(program, '9')
        mock_print.assert_called_once_with('1001')
