from math import atan, sqrt, degrees
from typing import List, Dict
from part_01 import parse


def run(asteroids: List[List[bool]], ox: int, oy: int) -> List[str]:
    angles = {}
    for y in range(len(asteroids)):
        for x in range(len(asteroids[y])):
            if x == ox and y == oy:
                continue
            if not asteroids[y][x]:
                continue
            dx, dy = x - ox, oy - y
            angle = get_angle(dx, dy)
            distance = sqrt((dx * dx) + (dy * dy))
            angle = f'{angle:07.3f}'
            if angle not in angles:
                angles[angle] = {}
            angles[angle][f'{x},{y}'] = distance

    for angle in angles:
        angles[angle] = sorted(angles[angle], key=angles[angle].get, reverse=True)

    i = 0
    sorted_angles = sorted(angles)
    vaporised = []
    while has_asteroids(angles):
        angle = sorted_angles[i % len(sorted_angles)]
        if angles[angle]:
            vaporised.append(angles[angle].pop())
        i += 1
    
    return vaporised

def has_asteroids(angles: Dict[str, List[str]]) -> bool:
    for angle in angles:
        if angles[angle]:
            return True
    return False


def get_angle(dx: int, dy: int) -> float:
    # 0 at top
    # 90 at right

    if dy > 0:
        if dx > 0:
            theta = degrees(atan(dx / dy))
        elif dx == 0:
            theta = 0.0
        else:
            theta = 360.0 - degrees(atan(abs(dx) / dy))

    elif dy == 0:
        if dx > 0:
            theta = 90.0
        else:
            theta = 270.0
    
    else:
        if dx > 0:
            theta = 180.0 - degrees(atan(dx / abs(dy)))
        elif dx == 0:
            theta = 180.0
        else:
            theta = 180.0 + degrees(atan(dx / dy))

    return theta


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        asteroids = f.readlines()

    asteroids = parse(asteroids)
    x, y = 14, 17

    vaporised = run(asteroids, x, y)

    print(f'200th asteroid to be vaporised at: {vaporised[199]}')
    xx, yy = (int(n) for n in vaporised[199].split(','))
    print(f'(x * 100) + y = {(xx * 100) + yy}')
