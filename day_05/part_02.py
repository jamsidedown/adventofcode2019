from typing import List


def run(p: List[str], input_parameter: str) -> str:
    i = 0
    while (p[i] != '99'):
        instruction = p[i].rjust(5, '0')
        opcode = int(instruction[-2:])
        modes = [instruction[2], instruction[1], instruction[0]]
        modes = [bool(int(mode)) for mode in modes]

        # add and multiply
        if opcode == 1 or opcode == 2:
            first = p[i + 1] if modes[0] else p[int(p[i + 1])]
            second = p[i + 2] if modes[1] else p[int(p[i + 2])]
            first, second = int(first), int(second)
            if opcode == 1:
                p[int(p[i + 3])] = str(first + second)
            else:
                p[int(p[i + 3])] = str(first * second)
            i += 4
        # input
        elif opcode == 3:
            p[int(p[i + 1])] = input_parameter
            i += 2
        # output
        elif opcode == 4:
            value = p[i + 1] if modes[0] else p[int(p[i + 1])]
            print(value)
            i += 2
        # jump if true or false
        elif opcode == 5 or opcode == 6:
            value = int(p[i + 1]) if modes[0] else int(p[int(p[i + 1])])
            jump = value != 0 if opcode == 5 else value == 0
            if jump:
                i = int(p[i + 2]) if modes[1] else int(p[int(p[i + 2])])
            else:
                i += 3
        # less than and equals
        elif opcode == 7 or opcode == 8:
            first = p[i + 1] if modes[0] else p[int(p[i + 1])]
            second = p[i + 2] if modes[1] else p[int(p[i + 2])]
            first, second = int(first), int(second)
            if opcode == 7:
                value = '1' if first < second else '0'
            else:
                value = '1' if first == second else '0'
            if modes[2]:
                p[i + 3] = value
            else:
                p[int(p[i + 3])] = value
            i += 4


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        program = f.read().split(',')

    run(program, '5')
