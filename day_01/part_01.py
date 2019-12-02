from typing import List


def run(masses: List[int]) -> int:
    return sum((mass // 3) - 2 for mass in masses)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        masses = [int(mass) for mass in f.readlines()]
    
    fuel = run(masses)
    print(f'Total fuel required: {fuel}')
