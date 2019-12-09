from collections import defaultdict
from typing import List


class IntcodeComputer:
    II = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2}

    def __init__(self, program: List[str]):
        self.program = defaultdict(lambda: 0, {i: int(x) for i, x in enumerate(program)})
        self.i = 0
        self.rbase = 0

    def run(self, input_parameter: int):
        if input_parameter is None:
            pass

        p = self.program
        i = self.i
        ii = self.II

        while (p[i] != 99):
            instruction = str(p[i]).rjust(5, '0')
            opcode = int(instruction[-2:])
            modes = [instruction[2], instruction[1], instruction[0]]
            modes = [int(mode) for mode in modes]

            if opcode == 99:
                break

            if opcode in {1, 2, 4, 5, 6, 7, 8, 9}:
                first = (p[p[i + 1]] if modes[0] == 0
                         else p[i + 1] if modes[0] == 1
                         else p[p[i + 1] + self.rbase])
            if opcode in {1, 2, 5, 6, 7, 8}:
                second = (p[p[i + 2]] if modes[1] == 0
                          else p[i + 2] if modes[1] == 1
                          else p[p[i + 2] + self.rbase])
            if opcode in {1, 2, 7, 8}:
                address = (p[i + 3] if modes[2] == 0
                           else i + 3 if modes[2] == 1
                           else p[i + 3] + self.rbase)

            if opcode == 1:
                p[address] = first + second
            elif opcode == 2:
                p[address] = first * second
            elif opcode == 3:
                address = (p[i + 1] if modes[0] == 0
                           else i + 1 if modes[0] == 1
                           else p[i + 1] + self.rbase)
                p[address] = input_parameter
            elif opcode == 4:
                print(first)
            elif opcode == 5:
                i = second - ii[opcode] if first != 0 else i
            elif opcode == 6:
                i = second - ii[opcode] if first == 0 else i
            elif opcode == 7:
                p[address] = int(first < second)
            elif opcode == 8:
                p[address] = int(first == second)
            elif opcode == 9:
                self.rbase += first
            else:
                print(f'problem opcode {opcode} at address {i}')

            i += ii[opcode]
            self.i = i


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        program = f.read().split(',')

    computer = IntcodeComputer(program)
    computer.run(1)
