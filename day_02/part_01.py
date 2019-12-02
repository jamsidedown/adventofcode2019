from typing import List


def run(program: List[int]) -> int:
    index = 0
    while True:
        op = program[index]

        if op == 99:
            break

        input_addr_1 = program[index + 1]
        input_addr_2 = program[index + 2]
        output_addr = program[index + 3]

        if op == 1:
            program[output_addr] = program[input_addr_1] + program[input_addr_2]
        elif op == 2:
            program[output_addr] = program[input_addr_1] * program[input_addr_2]
        else:
            return -1
        
        index += 4

    return program[0]

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        program = [int(op) for op in f.read().split(',')]

    program[1] = 12
    program[2] = 2
    print(run(program))
