masses = []

with open('input.txt', 'r') as f:
    masses = f.read().split('\n')

masses = [int(mass) for mass in masses if mass]
fuel = [(mass // 3) - 2 for mass in masses]

print(f'Total fuel required: {sum(fuel)}')
