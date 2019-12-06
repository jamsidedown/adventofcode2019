from typing import List


def run(orbits: List[str]) -> int:
    children = {}
    for orbit in orbits:
        split_orbit = orbit.split(')')
        child = split_orbit[1]
        parent = split_orbit[0]
        if child in children:
            print('problem child')
        children[child] = parent
    
    parents = {}
    for parent in children.values():
        if parent not in children:
            parents[parent] = 0
    
    while children:
        to_pop = []
        for child in children:
            if children[child] in parents:
                parents[child] = parents[children[child]] + 1
                to_pop.append(child)
        for child in to_pop:
            children.pop(child)
    
    sum = 0
    for parent in parents:
        sum += parents[parent]

    return sum


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        orbits = f.readlines()
    orbits = [orbit.strip() for orbit in orbits]
    total_orbits = run(orbits)
    print(f'total orbits: {total_orbits}')
