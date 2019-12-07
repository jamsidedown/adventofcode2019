import itertools
from typing import Iterable, List


class Amplifier:
    II = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}

    def __init__(self, program: List[str], phase_setting: int):
        self.program = [int(x) for x in program]
        self.phase = phase_setting
        self.i = 0
        self.inputs = 0

    def run(self, input_parameter: int) -> int:
        if input_parameter is None:
            return None

        p = self.program
        i = self.i
        ii = self.II

        while (p[i] != 99):
            instruction = str(p[i]).rjust(5, '0')
            opcode = int(instruction[-2:])
            modes = [instruction[2], instruction[1], instruction[0]]
            modes = [bool(int(mode)) for mode in modes]

            if opcode in {1, 2, 4, 5, 6, 7, 8}:
                first = p[i + 1] if modes[0] else p[p[i + 1]]
            if opcode in {1, 2, 5, 6, 7, 8}:
                second = p[i + 2] if modes[1] else p[p[i + 2]]
            if opcode in {1, 2, 7, 8}:
                address = i + 3 if modes[2] else p[i + 3]

            if opcode == 1:
                p[address] = first + second
            elif opcode == 2:
                p[address] = first * second
            elif opcode == 3:
                address = i + 1 if modes[0] else p[i + 1]
                p[address] = input_parameter if self.inputs > 0 else self.phase
                self.inputs += 1
            elif opcode == 4:
                self.i = i + ii[opcode]
                return first
            elif opcode == 5:
                i = second - ii[opcode] if first != 0 else i
            elif opcode == 6:
                i = second - ii[opcode] if first == 0 else i
            elif opcode == 7:
                p[address] = int(first < second)
            elif opcode == 8:
                p[address] = int(first == second)

            i += ii[opcode]
            self.i = i

        return None


def run_thrusters(program: List[str], phase_settings: Iterable[int]) -> int:
    amplifiers = []
    for phase_setting in phase_settings:
        amp = Amplifier(program, phase_setting)
        amplifiers.append(amp)
    
    output = 0
    while True:
        for amp in amplifiers:
            new_output = amp.run(output)
            if new_output is None:
                return output
            output = new_output
    
    return None


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        program = f.read().split(',')

    outputs = []
    inputs = {5, 6, 7, 8, 9}
    for phase_settings in itertools.permutations(inputs, 5):
        output = run_thrusters(program, phase_settings)
        outputs.append(output)

    print(f'max output: {max(outputs)}')

