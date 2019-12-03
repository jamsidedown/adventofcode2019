import re
from typing import List, Tuple


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return f'{self.x},{self.y}'


instruction_regex = re.compile(r'^([UDLR])(\d+)$')


def run(wires: List[List[str]]) -> int:
    wire_paths = []

    for wire in wires:
        coords = Point(0, 0, 0)
        wire_points = {}
        for instruction in wire:
            direction, distance = _parse_instruction(instruction)
            for i in range(1, distance + 1):
                if direction == 'U':
                    coords.y += 1
                elif direction == 'D':
                    coords.y -= 1
                elif direction == 'R':
                    coords.x += 1
                elif direction == 'L':
                    coords.x -= 1
                coords.z += 1
                
                str_coords = str(coords)
                if str_coords not in wire_points:
                    wire_points[str_coords] = coords.z
        
        wire_paths.append(wire_points)

    collisions = set(wire_paths[0]) & set(wire_paths[1])

    distances = []
    for collision in collisions:
        distance = wire_paths[0][collision] + wire_paths[1][collision]
        distances.append(distance)

    return min(distances)


def _parse_instruction(instruction: str) -> Tuple[str, int]:
    re_match = instruction_regex.match(instruction)
    direction = re_match.group(1)
    distance = int(re_match.group(2))
    return direction, distance


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        wires = f.readlines()

    wires = [wire.split(',') for wire in wires]
    distance = run(wires)

    print(f'closest intersection: {distance}')
