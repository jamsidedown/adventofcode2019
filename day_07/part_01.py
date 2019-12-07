from collections import deque
import itertools
from typing import List, Deque


def run(program: List[str], input_parameters: Deque[int]) -> int:
    p = [int(x) for x in program]
    i = 0
    ii = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4}

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
            p[address] = input_parameters.popleft()
        elif opcode == 4:
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
    
    return -1


def run_thrusters(program: List[str], phase_settings: Deque[int]) -> int:
    output = 0
    while phase_settings:
        input_parameters = deque([phase_settings.popleft(), output])
        output = run(program, input_parameters)
    return output


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        program = f.read().split(',')

    outputs = []
    inputs = {0, 1, 2, 3, 4}
    for combination in itertools.permutations(inputs, 5):
        phase_settings = deque(combination)
        output = run_thrusters(program, phase_settings)
        outputs.append(output)
    
    print(f'max output: {max(outputs)}')
        
