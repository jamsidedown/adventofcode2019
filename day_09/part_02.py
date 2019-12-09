from part_01 import IntcodeComputer


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        program = f.read().split(',')

    computer = IntcodeComputer(program)
    computer.run(2)
