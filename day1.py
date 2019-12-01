from typing import List
masses: List[int] = []
with open('./inputs/day1.txt', 'r') as f:
    line = f.readline()
    while line:
        masses.append(int(line))
        line = f.readline()


def fuel(mass: int):
    return mass//3 - 2


if __name__ == "__main__":
    result = [fuel(x) for x in masses]
    print(sum(result))
