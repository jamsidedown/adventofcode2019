masses = []

calc_fuel = lambda m : (m // 3) - 2

with open('input.txt', 'r') as f:
    masses = f.read().split('\n')

masses = [int(mass) for mass in masses if mass]
fuel = [calc_fuel(mass) for mass in masses]

for i, f in enumerate(fuel):
    running = calc_fuel(f)
    while running > 0:
        fuel[i] += running
        running = calc_fuel(running)

print(f'Total fuel required: {sum(fuel)}')
