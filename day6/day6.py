from typing import List, Tuple, NamedTuple, DefaultDict
from collections import defaultdict

TEST = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""


class Pair(NamedTuple):
    planet: str  # from
    orbit: str  # to


def create_from(data: str):
    p, o = data.strip().split(')')
    return Pair(p, o)


pairs = [create_from(data) for data in TEST.strip().split('\n')]


def graph(pairs: List[Pair]):
    """Creates a graph bottom up (from orbit to planet)"""
    graph = {}
    for (planet, orbit) in pairs:
        graph[orbit] = planet
    return graph


def indirectly(start: str, graph: DefaultDict[str, str]):
    num = 0
    while start != "COM":
        num += 1
        start = graph[start]
    return num


g = graph(pairs)

assert indirectly('D', g) == 3
assert indirectly('L', g) == 7
assert indirectly('COM', g) == 0


def total(pairs: List[Pair], g: DefaultDict[str, str]):
    num = 0
    for each in pairs:
        num += indirectly(each.planet, g)
    return num + len(g)


assert total(pairs, g) == 42

with open('input.txt') as f:
    data = ''.join(x for x in f)


def solution(data: str):
    pairs = [create_from(d) for d in data.strip().split('\n')]
    g = graph(pairs)
    return total(pairs, g)


print(solution(data))


TEST2 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""


pairs = [create_from(data) for data in TEST2.strip().split('\n')]
g = graph(pairs)

start1 = 'YOU'
path1 = []
start2 = 'SAN'
path2 = []
count = 0
while g[start1] != 'COM':
    path1.append(g[start1])
    start1 = g[start1]

while g[start2] != 'COM':
    path2.append(g[start2])
    start2 = g[start2]

# find shortest common subsequence:

while path1[-1] == path2[-1]:
    path1.pop()
    path2.pop()

if g[path1[-1]] == g[path2[-1]]:
    assert (len(path1) + len(path2)) == 4


def shortest_path(data: str):
    pairs = [create_from(d) for d in data.strip().split('\n')]
    g = graph(pairs)
    start1 = 'YOU'
    path1 = []
    start2 = 'SAN'
    path2 = []
    while g[start1] != 'COM':
        path1.append(g[start1])
        start1 = g[start1]
    while g[start2] != 'COM':
        path2.append(g[start2])
        start2 = g[start2]
    while path1[-1] == path2[-1]:
        path1.pop()
        path2.pop()
    if g[path1[-1]] == g[path2[-1]]:
        return len(path1) + len(path2)


print(shortest_path(data))
