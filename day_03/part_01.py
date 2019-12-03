import re
from typing import List, NamedTuple


class Point(NamedTuple):
    x: int
    y: int


class Line(NamedTuple):
    start: Point
    end: Point


instruction_regex = re.compile(r'^([UDLR])(\d+)$')


def run(wires: List[List[str]]) -> int:
    lines = []

    for wire in wires:
        coords = Point(0, 0)
        wire_lines = []
        for instruction in wire:
            re_match = instruction_regex.match(instruction)
            direction = re_match.group(1)
            distance = int(re_match.group(2))
            if direction == 'U':
                new_coords = Point(coords.x, coords.y + distance)
            elif direction == 'D':
                new_coords = Point(coords.x, coords.y - distance)
            elif direction == 'R':
                new_coords = Point(coords.x + distance, coords.y)
            elif direction == 'L':
                new_coords = Point(coords.x - distance, coords.y)
            
            wire_lines.append(Line(coords, new_coords))
            coords = new_coords
        lines.append(wire_lines)

    collisions = []
    for first_line in lines[0]:
        for second_line in lines[1]:
            intercept = _collision(first_line, second_line)
            if intercept and not (intercept.x == 0 and intercept.y == 0):
                collisions.append(intercept)

    distances = []
    for collision in collisions:
        distance = abs(collision.x) + abs(collision.y)
        distances.append(distance)

    return min(distances)


def _collision(first: Line, second: Line) -> Point:
    if _is_vertical(first) and _is_vertical(second):
        return None
    
    if _is_vertical(first):
        vertical = first
        horizontal = second
    else:
        vertical = second
        horizontal = first
    
    if (vertical.start.x <= max(horizontal.start.x, horizontal.end.x) and 
            vertical.start.x >= min(horizontal.start.x, horizontal.end.x) and
            horizontal.start.y <= max(vertical.start.y, vertical.end.y) and
            horizontal.start.y >= min(vertical.start.y, vertical.end.y)):
        return Point(vertical.start.x, horizontal.start.y)

    return None


def _is_vertical(line: Line) -> bool:
    return line.start.x == line.end.x


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        wires = f.readlines()
    
    wires = [wire.split(',') for wire in wires]
    distance = run(wires)

    print(f'closest intersection: {distance}')
