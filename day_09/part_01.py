from typing import List


class IntcodeComputer:
    II = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2}

    def __init__(self, program: List[str]):
        self.program = {i: int(x) for i, x in enumerate(program)}
        self.i = 0
        self.rbase = 0

    def run(self, input_parameter: int):
        if input_parameter is None:
            pass

        p = self.program
        i = self.i
        ii = self.II

        while (p[i] != 99):
            instruction = str(p.get(i, 0)).rjust(5, '0')
            opcode = int(instruction[-2:])
            modes = [instruction[2], instruction[1], instruction[0]]
            # mode 0: position mode
            # mode 1: immediate mode
            # mode 2: relative mode
            modes = [int(mode) for mode in modes]

            if opcode == 99:
                break

            if opcode in {1, 2, 4, 5, 6, 7, 8, 9}:
                if modes[0] == 0:
                    first = p.get(p.get(i + 1, 0), 0)
                elif modes[0] == 1:
                    first = p.get(i + 1, 0)
                elif modes[0] == 2:
                    first = p.get(p.get(i + 1, 0) + self.rbase, 0)
                else:
                    print(f'problem mode {modes[0]} at address {i}')
            if opcode in {1, 2, 5, 6, 7, 8}:
                if modes[1] == 0:
                    second = p.get(p.get(i + 2, 0), 0)
                elif modes[1] == 1:
                    second = p.get(i + 2, 0)
                elif modes[1] == 2:
                    second = p.get(p.get(i + 2, 0) + self.rbase, 0)
                else:
                    print(f'problem mode {modes[1]} at address {i}')
            if opcode in {1, 2, 7, 8}:
                if modes[2] == 0:
                    address = p.get(i + 3, 0)
                elif modes[2] == 1:
                    address = i + 3
                elif modes[2] == 2:
                    address = p.get(i + 3, 0) + self.rbase
                else:
                    print(f'problem mode {modes[2]} at address {i}')

            if opcode == 1:
                p[address] = first + second
            elif opcode == 2:
                p[address] = first * second
            elif opcode == 3:
                if modes[0] == 0:
                    address = p.get(i + 1, 0)
                elif modes[0] == 1:
                    address = i + 1
                else:
                    address = p.get(i + 1, 0) + self.rbase
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
