from typing import List
from part_01 import run


def find_answer(program: List[int], target: int) -> int:
    for noun in range(100):
        for verb in range(100):
            program_copy = [*program]
            program_copy[1] = noun
            program_copy[2] = verb
            result = run(program_copy)
            if result == target:
                print(f'noun: {noun}')
                print(f'verb: {verb}')
                return (100 * noun) + verb


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        program = [int(op) for op in f.read().split(',')]

    answer = find_answer(program, 19690720)
    print(f'answer: {answer}')

    

