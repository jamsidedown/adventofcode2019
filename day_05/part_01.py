from typing import List


def run(p: List[str], input_parameter: int):
    for i in range(len(p)):
        p[i] = int(p[i])

    i = 0
    ii = {1: 4, 2: 4, 3: 2, 4: 2}

    while (p[i] != 99):
        instruction = str(p[i]).rjust(5, '0')
        opcode = int(instruction[-2:])
        modes = [instruction[2], instruction[1], instruction[0]]
        modes = [bool(int(mode)) for mode in modes]

        if opcode in {1, 2, 4}:
            first = p[i + 1] if modes[0] else p[p[i + 1]]
        if opcode in {1, 2}:
            second = p[i + 2] if modes[1] else p[p[i + 2]]
        if opcode in {1, 2}:
            address = i + 3 if modes[2] else p[i + 3]

        if opcode == 1:
            p[address] = first + second
        elif opcode == 2:
            p[address] = first * second
        elif opcode == 3:
            address = i + 1 if modes[0] else p[i + 1]
            p[address] = input_parameter
        elif opcode == 4:
            print(first)
        
        i += ii[opcode]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        program = f.read().split(',')
    run(program, 1)
