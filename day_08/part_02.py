from typing import List
from part_01 import get_layers


def flatten(layers: List[List[List[int]]]) -> List[List[int]]:
    flattened = []
    visible = {0, 1}
    for layer in reversed(layers):
        if not flattened:
            flattened = layer
            pass
        height = len(layer)
        for y in range(height):
            row = layer[y]
            width = len(row)
            for x in range(width):
                pixel = row[x]
                if pixel in visible:
                    flattened[y][x] = pixel

    return flattened


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        valids = {str(x) for x in range(10)}
        image = [int(x) for x in f.read() if x in valids]

    layers = get_layers(image, 25, 6)
    flattened = flatten(layers)

    colours = {0: '■', 1: '□', 2: ' '}
    for row in flattened:
        print(''.join([colours[pixel] for pixel in row]))
