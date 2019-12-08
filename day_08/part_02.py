from typing import List
from part_01 import get_layers


def flatten(layers: List[List[List[int]]]) -> List[List[int]]:
    flattened = []
    for layer in reversed(layers):
        if not flattened:
            flattened = layer
            pass
        for y in range(len(layer)):
            row = layer[y]
            for x in range(len(row)):
                pixel = row[x]
                if pixel in {0, 1}:
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
