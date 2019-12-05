from math import log10, floor
from typing import List


def run(p: List[str]) -> int:
    input_parameter = 1
    i = 0
    while (p[i] != '99'):
        instruction = p[i]
        opcode = int(instruction[-2:])
        modes = [False, False, False]


        if opcode == 1:
            p[p[i + 3]] = p[p[i + 1]] + p[p[i + 2]]
            i += 4
        elif opcode == 2:
            p[p[i + 3]] = p[p[i + 1]] * p[p[i + 2]]
            i += 4
        elif opcode == 3:
            p[p[i + 1]] = input_parameter
            p += 2
        elif opcode == 4:
            print(p[p[i + 1]])
            p += 2
    return p[0]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        program = f.read().split(',')
    
    print(run(program))
