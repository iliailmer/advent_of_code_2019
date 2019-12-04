from collections import OrderedDict
from typing import List, Tuple, Callable
with open('input.txt') as f:
    data = [x.strip('\n').split(',') for x in f.readlines()]


class Wire:
    def __init__(self, sequence: List[str]):
        self.x = self.y = 0
        self.visited: List[Tuple[int, int]] = []
        self.sequence = sequence
        self.steps: List[int] = []

    def __repr__(self):
        return f"Wire at ({self.x},{self.y})"


def moveup(obj: Wire, steps2get_here: int) -> None:
    obj.y += 1
    obj.visited.append((obj.x, obj.y))
    obj.steps.append(steps2get_here)


def moveleft(obj: Wire, steps2get_here: int) -> None:
    obj.x -= 1
    obj.visited.append((obj.x, obj.y))
    obj.steps.append(steps2get_here)


def moveright(obj: Wire, steps2get_here: int) -> None:
    obj.x += 1
    obj.visited.append((obj.x, obj.y))
    obj.steps.append(steps2get_here)


def movedown(obj: Wire, steps2get_here: int) -> None:
    obj.y -= 1
    obj.visited.append((obj.x, obj.y))
    obj.steps.append(steps2get_here)


moves: dict = dict()

moves['R'] = moveright
moves['U'] = moveup
moves['L'] = moveleft
moves['D'] = movedown


# w1 = Wire(['R8', 'U5', 'L5', 'D3'])
# w2 = Wire(['U7', 'R6', 'D4', 'L4'])


def place_wire(wire: Wire) -> None:
    """"Places" the wire by following the sequence"""
    steps2get_here = 0
    for move in wire.sequence:
        direction = move[0]
        distance = int(move[1:])
        for _ in range(distance):
            steps2get_here += 1
            moves[direction](wire, steps2get_here)


def manhattan_distance(point: Tuple[int, int]) -> int:
    """Calculates Manhattan distance to 0"""
    return abs(point[0]) + abs(point[1])


def solution_part1(seq1: List[str], seq2: List[str]) -> int:
    w1 = Wire(seq1)
    place_wire(w1)
    w2 = Wire(seq2)
    place_wire(w2)
    intersection = set([(x[0], x[1]) for x in w1.visited])\
        .intersection(set([(x[0], x[1]) for x in w2.visited]))
    distances = [manhattan_distance(point) for point in intersection]
    return min(distances)


assert solution_part1(['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']) == 6
assert solution_part1(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
                      ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']) == 159
assert solution_part1(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
                      ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']) == 135


print(solution_part1(data[0], data[1]))


# Part Two
seq1 = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
seq2 = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']


def solution_part2(seq1: List[str], seq2: List[str]):
    """This is painfully slow, I am sorry"""
    w1 = Wire(seq1)
    place_wire(w1)
    w2 = Wire(seq2)
    place_wire(w2)
    ans = []
    for each in (set(w1.visited).intersection(set(w2.visited))):
        ans.append(w1.steps[w1.visited.index(each)] +
                   w2.steps[w2.visited.index(each)])
    return min(ans)


assert solution_part2(['R8', 'U5', 'L5', 'D3'], ['U7', 'R6', 'D4', 'L4']) == 30
assert solution_part2(['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72'],
                      ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']) == 610
assert solution_part2(['R98', 'U47', 'R26', 'D63', 'R33', 'U87', 'L62', 'D20', 'R33', 'U53', 'R51'],
                      ['U98', 'R91', 'D20', 'R16', 'D67', 'R40', 'U7', 'R15', 'U6', 'R7']) == 410

print(solution_part2(data[0], data[1]))
