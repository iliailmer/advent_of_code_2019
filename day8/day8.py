"""Day 8.

To make sure the image wasn't corrupted during transmission,
the Elves would like you to find the layer that contains the fewest 0 digits.
On that layer, what is the number of 1
digits multiplied by the number of 2 digits?
"""

from typing import List
from collections import Counter
with open('input.txt') as f:
    image = f.readline()


def get_layers(image: str, width: int, height: int):
    """Reshape a list."""
    data = [int(x) for x in image]
    n = len(data)
    layers = [[] for _ in range(n//(width*height))]
    for layer in layers:
        for i in range(height):
            row = data[:width]
            data = data[width:]
            layer.append(row)
    return layers


def display(layers):
    """Output a layer."""
    for layer in layers:
        for row in layer:
            print(row)
        print('\n')
    print('\n')


layers = get_layers(image, 25, 6)


def part1(layers: List[List[int]]):
    """Solve part 1."""
    zeros = {'0': 100000000}
    for (idx, layer) in enumerate(layers):
        # unwrap layer
        counter = Counter(''.join(str(x)
                                  for x in [i for l in layer for i in l]))
        if zeros['0'] > counter['0']:
            zeros = counter
    return zeros['1']*zeros['2']


k = 0
sym = {0: '0', 1: '1'}
output = [[0 for _ in range(25)] for _ in range(6)]
for i in range(6):
    for j in range(25):
        while layers[k][i][j] == 2 and k < 100:
            k += 1
        output[i][j] = sym[layers[k][i][j]]
        k = 0


for row in output:
    print(''.join(row))
