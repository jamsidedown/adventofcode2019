from typing import List


def run(orbits: List[str]) -> int:
    parents = {}
    for orbit in orbits:
        split_orbit = orbit.split(')')
        child = split_orbit[1]
        parent = split_orbit[0]
        parents[child] = parent
    
    san_parent = parents['SAN']
    you_parent = parents['YOU']

    san_parents = {san_parent: 0}

    jumps = 0
    while san_parent in parents:
        san_parent = parents[san_parent]
        jumps += 1
        san_parents[san_parent] = jumps
    
    jumps = 0
    while you_parent not in san_parents:
        you_parent = parents[you_parent]
        jumps += 1

    return jumps + san_parents[you_parent]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        orbits = f.readlines()
    orbits = [orbit.strip() for orbit in orbits]
    total_jumps = run(orbits)
    print(f'total jumps: {total_jumps}')
