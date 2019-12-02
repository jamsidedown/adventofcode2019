from typing import List


def run(p: List[int]) -> int:
    for i in range(0, len(p), 4):
        if p[i] == 99:
            return p[0]
        elif p[i] == 1:
            p[p[i + 3]] = p[p[i + 1]] + p[p[i + 2]]
        elif p[i] == 2:
            p[p[i + 3]] = p[p[i + 1]] * p[p[i + 2]]
    return -1


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        program = [int(op) for op in f.read().split(',')]

    program[1] = 12
    program[2] = 2
    print(run(program))
