from typing import List


masses: List[int] = []
with open('./inputs/day1.txt', 'r') as f:
    line = f.readline()
    while line:
        masses.append(int(line))
        line = f.readline()


def fuel(mass: int) -> int:
    return max(mass//3 - 2, 0)


def full_fuel(mass: List[int]) -> int:
    s = 0
    for i in range(len(mass)):
        old_mass = mass[i]
        new_mass = 0
        while fuel(old_mass) != 0:
            new_mass = fuel(old_mass)
            old_mass = new_mass
            s += new_mass
    return s


if __name__ == "__main__":
    part1 = [fuel(x) for x in masses]
    print(sum(part1))
    part2 = [full_fuel([x]) for x in masses]
    print(sum(part2))
