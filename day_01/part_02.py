from typing import List


def run(masses: List[int]) -> int:
    calc_fuel = lambda m : (m // 3) - 2
    fuel = [calc_fuel(mass) for mass in masses]

    for i, f in enumerate(fuel):
        running = calc_fuel(f)
        while running > 0:
            fuel[i] += running
            running = calc_fuel(running)
    
    return sum(fuel)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        masses = f.read().split('\n')
        masses = [int(mass) for mass in masses if mass]
        fuel = run(masses)

        print(f'Total fuel required: {fuel}')
