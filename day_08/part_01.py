from typing import List


def run(image: List[int], width: int, height: int) -> List:
    layers = []
    i = 0
    pixels = width * height
    while i < len(image):
        layer = i // pixels
        if layer >= len(layers):
            layers.append([])
        row = (i % pixels) // width
        if row >= len(layers[layer]):
            layers[layer].append([])
        layers[layer][row].append(image[i])
        i += 1

    return layers


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        valids = {str(x) for x in range(10)}
        image = [int(x) for x in f.read() if x in valids]
    layers = run(image, 25, 6)

    zero_counts = [sum(row.count(0) for row in layer) for layer in layers]
    layer_index = zero_counts.index(min(zero_counts))

    layer = layers[layer_index]
    ones = sum(row.count(1) for row in layer)
    twos = sum(row.count(2) for row in layer)

    product = ones * twos
    print(product)
