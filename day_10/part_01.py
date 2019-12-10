from typing import List, Tuple


def run(asteroids: List[List[bool]]) -> Tuple[str, int]:
    counts = {}
    height = len(asteroids)
    width = len(asteroids[0])
    for y in range(height):
        for x in range(width):
            if not asteroids[y][x]:
                continue
            key = f'{x},{y}'
            count = get_count(x, y, asteroids)
            counts[key] = count
    
    max_key = None
    max_count = 0
    for key in counts:
        if counts[key] >= max_count:
            max_count = counts[key]
            max_key = key

    return max_key, max_count


def get_count(x: int, y: int, asteroids: List[List[bool]]) -> int:
    asteroid_map = [[*row] for row in asteroids]
    asteroid_map[y][x] = False
    height = len(asteroids)
    width = len(asteroids[0])
    count = 0
    for d in range(max(width, height)):
        for xx in range(x - d, x + d + 1):
            if xx < 0 or xx >= width:
                continue
            for yy in range(y - d, y + d + 1):
                if yy < 0 or yy >= height:
                    continue
                if asteroid_map[yy][xx]:
                    count += 1
                    dx = xx - x
                    dy = yy - y

                    for d in range(2, max(width, height)):
                        while dx % d == 0 and dy % d == 0:
                            dx //= d
                            dy //= d

                    for m in range(1, max(width, height)):
                        mx = x + (m * dx)
                        my = y + (m * dy)
                        if in_bounds(mx, my, width, height):
                            asteroid_map[my][mx] = False
                        else:
                            break

    return count


def in_bounds(x: int, y: int, width: int, height: int) -> bool:
    return x >= 0 and y >= 0 and x < width and y < height


def parse(asteroids: List[str]) -> List[List[bool]]:
    return [[char == '#' for char in line] for line in asteroids]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        asteroids = f.readlines()

    asteroids = parse(asteroids)
    coords, count = run(asteroids)

    print(f'best location at {coords}, {count} asteroids detected')
