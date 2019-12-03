from typing import List
from part_01 import parse_instruction


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
    
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
        self.z += 1


def run(wires: List[List[str]]) -> int:
    wire_paths = []

    for wire in wires:
        coords = Point(0, 0, 0)
        wire_points = {}
        for instruction in wire:
            direction, distance = parse_instruction(instruction)
            for _ in range(distance):
                coords.move(direction)
                if str(coords) not in wire_points:
                    wire_points[str(coords)] = coords.z
        
        wire_paths.append(wire_points)

    collisions = set(wire_paths[0]) & set(wire_paths[1])
    distances = [wire_paths[0][collision] + wire_paths[1][collision] for collision in collisions]

    return min(distances)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        wires = f.readlines()

    wires = [wire.split(',') for wire in wires]
    distance = run(wires)

    print(f'closest intersection: {distance}')
