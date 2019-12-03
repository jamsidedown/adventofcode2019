import re
from typing import List, Tuple


INSTRUCTION_REGEX = re.compile(r'^([UDLR])(\d+)$')


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x},{self.y}'

    def move(self, direction: str):
        if direction == 'U':
            self.y += 1
        elif direction == 'D':
            self.y -= 1
        elif direction == 'R':
            self.x += 1
        elif direction == 'L':
            self.x -= 1
    
    @property
    def distance(self):
        return abs(self.x) + abs(self.y)


def run(wires: List[List[str]]) -> int:
    wire_paths = []

    for wire in wires:
        coords = Point(0, 0)
        wire_points = {}
        for instruction in wire:
            direction, distance = parse_instruction(instruction)
            for _ in range(distance):
                coords.move(direction)
                wire_points[str(coords)] = coords.distance

        wire_paths.append(wire_points)

    collisions = set(wire_paths[0]) & set(wire_paths[1])
    distances = [wire_paths[0][collision] for collision in collisions]

    return min(distances)


def parse_instruction(instruction: str) -> Tuple[str, int]:
    re_match = INSTRUCTION_REGEX.match(instruction)
    return re_match.group(1), int(re_match.group(2))


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        wires = f.readlines()
    
    wires = [wire.split(',') for wire in wires]
    distance = run(wires)

    print(f'closest intersection: {distance}')
