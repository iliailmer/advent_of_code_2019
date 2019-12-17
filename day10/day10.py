"""Solution to day 10."""

from typing import List
from collections import defaultdict
from typing import Tuple, NamedTuple


class Asteroid(NamedTuple):
    x: int
    y: int


asteroids = []
with open("input.txt") as f:
    asteroids = [list(x.strip('\n')) for x in f.readlines()]


def display(layers):
    """Output a layer."""
    for layer in layers:
        for row in layer:
            print(row)
        print('\n')


display([asteroids])


MAX_X = len(asteroids[0])
MAX_Y = len(asteroids)
counter = [[0 for _ in asteroids[0]] for _ in asteroids]
# Learn to check the quadrant on the lower left
lower_left = []
x, y = (2, 2)
visited = defaultdict(Tuple[int, int])

inputs = [Asteroid(j, i) for i in range(len(asteroids)) for j in range(
    len(asteroids[0]))if asteroids[i][j] == '#']


def check_left(start: Asteroid, counter: List[int]):
    x_ = start.x-1
    while x_ >= 0:
        if asteroids[start.y][x_] != '#':
            x_ -= 1
        else:
            counter[start.y][start.x] += 1
            break
    return counter


def check_right(start: Asteroid, counter: List[int]):
    x_ = start.x + 1
    while x_ < MAX_X:
        if asteroids[start.y][x_] != '#':
            x_ += 1
        else:
            counter[start.y][start.x] += 1
            break
    return counter


def check_below(start: Asteroid, counter: List[int]):
    y_ = start.y + 1
    while y_ < MAX_Y:
        if asteroids[y_][start.x] != '#':
            y_ += 1
        else:
            counter[start.y][start.x] += 1
            break
    return counter


def check_above(start: Asteroid, counter: List[int]):
    y_ = start.y-1
    while y_ >= 0:
        if asteroids[y_][start.x] != '#':
            y_ -= 1
        else:
            counter[start.y][start.x] += 1
            break
    return counter


def check_first_quad(start: Asteroid, counter: List[int],
                     asteroids: List[str]):
    x_ = start.x + 1
    y_ = 0
    forbidden = []
    while x_ < MAX_X:
        while y_ < start.y:
            if (x_, y_) not in forbidden:
                if asteroids[y_][x_] != '#':
                    y_ += 1
                else:
                    counter[start.y][start.x] += 1
                    dx = abs(x_ - start.x)
                    dy = abs(start.y - y_)
                    forbidden += list(zip(range(x_, MAX_X, dx),
                                          range(y_, -1, -dy)))
                    y_ += 1
            else:
                y_ += 1
        x_ += 1
        y_ = 0
    return counter


def check_second_quad(start: Asteroid, counter: List[int],
                      asteroids: List[str]):
    x_ = start.x - 1
    y_ = 0
    forbidden = []
    while x_ >= 0:
        while y_ < start.y:
            if (x_, y_) not in forbidden:
                if asteroids[y_][x_] != '#':
                    y_ += 1
                else:
                    counter[start.y][start.x] += 1
                    dx = abs(start.x - x_)
                    dy = abs(start.y - y_)
                    forbidden += list(zip(range(x_, -1, -dx),
                                          range(y_, -1, -dy)))
                    y_ += 1
            else:
                y_ += 1
        x_ -= 1
        y_ = 0
    return counter


def check_third_quad(start: Asteroid, counter: List[int],
                     asteroids: List[str]):
    x_ = start.x - 1
    y_ = start.y + 1
    forbidden = []
    while x_ >= 0:
        while y_ < MAX_Y:
            if (x_, y_) not in forbidden:
                if asteroids[y_][x_] != '#':
                    y_ += 1
                else:
                    counter[start.y][start.x] += 1
                    dx = abs(start.x - x_)
                    dy = abs(y_ - start.y)
                    forbidden += list(zip(range(x_, -1, -dx),
                                          range(y_, MAX_Y, dy)))
                    y_ += 1
            else:
                y_ += 1
        x_ -= 1
        y_ = start.y + 1
    return counter


def check_fourth_quad(start: Asteroid, counter: List[int],
                      asteroids: List[str]):
    x_ = start.x + 1
    y_ = start.y + 1
    forbidden = []
    while x_ < MAX_X:
        while y_ < MAX_Y:
            if (x_, y_) not in forbidden:
                if asteroids[y_][x_] != '#':
                    y_ += 1
                else:
                    counter[start.y][start.x] += 1
                    dx = abs(start.x - x_)
                    dy = abs(y_ - start.y)
                    forbidden += list(zip(range(x_, MAX_X, dx),
                                          range(y_, MAX_Y, dy)))
                    y_ += 1
            else:
                y_ += 1
        x_ += 1
        y_ = start.y + 1
    return counter


def vaporize_first_quad(start: Asteroid, counter: List[int],
                        asteroids: List[str]):
    x_ = start.x + 1
    y_ = 0
    forbidden = []
    while x_ < MAX_X:
        while y_ < start.y:
            if (x_, y_) not in forbidden:
                if asteroids[y_][x_] != '#':
                    y_ += 1
                else:
                    asteroids[y_][x_] = '.'
                    counter[start.y][start.x] += 1
                    dx = abs(x_ - start.x)
                    dy = abs(start.y - y_)
                    forbidden += list(zip(range(x_, MAX_X, dx),
                                          range(y_, -1, -dy)))
                    y_ += 1
            else:
                y_ += 1
        x_ += 1
        y_ = 0
    return counter


def vaporize_second_quad(start: Asteroid, counter: List[int],
                         asteroids: List[str]):
    x_ = start.x - 1
    y_ = 0
    forbidden = []
    while x_ >= 0:
        while y_ < start.y:
            if (x_, y_) not in forbidden:
                if asteroids[y_][x_] != '#':
                    y_ += 1
                else:
                    asteroids[y_][x_] = '.'
                    counter[start.y][start.x] += 1
                    dx = abs(start.x - x_)
                    dy = abs(start.y - y_)
                    forbidden += list(zip(range(x_, -1, -dx),
                                          range(y_, -1, -dy)))
                    y_ += 1
            else:
                y_ += 1
        x_ -= 1
        y_ = 0
    return counter


def vaporize_third_quad(start: Asteroid, counter: List[int],
                        asteroids: List[str]):
    x_ = start.x - 1
    y_ = start.y + 1
    forbidden = []
    while x_ >= 0:
        while y_ < MAX_Y:
            if (x_, y_) not in forbidden:
                if asteroids[y_][x_] != '#':
                    y_ += 1
                else:
                    asteroids[y_][x_] = '.'
                    counter[start.y][start.x] += 1
                    dx = abs(start.x - x_)
                    dy = abs(y_ - start.y)
                    forbidden += list(zip(range(x_, -1, -dx),
                                          range(y_, MAX_Y, dy)))
                    y_ += 1
            else:
                y_ += 1
        x_ -= 1
        y_ = start.y + 1
    return counter


def vaporize_fourth_quad(start: Asteroid, counter: List[int],
                         asteroids: List[str]):
    x_ = start.x + 1
    y_ = start.y + 1
    forbidden = []
    while x_ < MAX_X:
        while y_ < MAX_Y:
            if (x_, y_) not in forbidden:
                if asteroids[y_][x_] != '#':
                    y_ += 1
                else:
                    asteroids[y_][x_] = '.'
                    counter[start.y][start.x] += 1
                    dx = abs(start.x - x_)
                    dy = abs(y_ - start.y)
                    forbidden += list(zip(range(x_, MAX_X, dx),
                                          range(y_, MAX_Y, dy)))
                    y_ += 1
            else:
                y_ += 1
        x_ += 1
        y_ = start.y + 1
    return counter


def vaporize_left(start: Asteroid, counter: List[int]):
    x_ = start.x-1
    while x_ >= 0:
        if asteroids[start.y][x_] != '#':
            x_ -= 1
        else:
            asteroids[start.y][x_] = '.'
            counter[start.y][start.x] += 1
            break
    return counter


def vaporize_right(start: Asteroid, counter: List[int]):
    x_ = start.x + 1
    while x_ < MAX_X:
        if asteroids[start.y][x_] != '#':
            x_ += 1
        else:
            asteroids[start.y][x_] = '.'
            counter[start.y][start.x] += 1
            break
    return counter


def vaporize_below(start: Asteroid, counter: List[int]):
    y_ = start.y + 1
    while y_ < MAX_Y:
        if asteroids[y_][start.x] != '#':
            y_ += 1
        else:
            asteroids[y_][start.x] = '.'
            counter[start.y][start.x] += 1
            break
    return counter


def vaporize_above(start: Asteroid, counter: List[int]):
    y_ = start.y-1
    while y_ >= 0:
        if asteroids[y_][start.x] != '#':
            y_ -= 1
        else:
            asteroids[y_][start.x] = '.'
            counter[start.y][start.x] += 1
            break
    return counter


# display([asteroids])
for each in inputs:
    counter = check_right(each, counter)
    counter = check_above(each, counter)
    counter = check_left(each, counter)
    counter = check_below(each, counter)
    counter = check_first_quad(each, counter, asteroids)
    counter = check_second_quad(each, counter, asteroids)
    counter = check_third_quad(each, counter, asteroids)
    counter = check_fourth_quad(each, counter, asteroids)

display([asteroids, counter])

print(max(counter))

while not any(200 in row for row in counter):
    for each in inputs:
        counter = vaporize_above(each, counter)
        counter = vaporize_first_quad(each, counter, asteroids)

        counter = vaporize_left(each, counter)
        counter = vaporize_fourth_quad(each, counter, asteroids)

        counter = vaporize_below(each, counter)
        counter = vaporize_third_quad(each, counter, asteroids)

        counter = vaporize_right(each, counter)
        counter = vaporize_second_quad(each, counter, asteroids)
    display([asteroids])

display([asteroids, counter])
