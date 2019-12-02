from typing import List


def run(masses: List[int]) -> int:
    return sum(_calc_fuel(mass) for mass in masses)


def _calc_fuel(mass: int) -> int:
    fuel = (mass // 3) - 2
    return fuel + _calc_fuel(fuel) if fuel > 0 else 0


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        masses = [int(mass) for mass in f.readlines()]

    fuel = run(masses)
    print(f'Total fuel required: {fuel}')
