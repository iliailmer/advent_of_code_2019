from collections import Counter


def is_six_digit(number: int) -> bool:
    return len(list(str(number))) == 6


def is_within(number: int, left: int, right: int) -> bool:
    return (number <= right) and (number >= left)


def two_adj(number: int) -> bool:
    return any([x == y for (x, y) in zip(str(number), str(number)[1:])])


def never_decrease(number: int) -> bool:
    num = str(number)
    ans = True
    for i in range(len(num)-1):
        # probably could be improved using "all"
        ans = ans and (int(num[i]) <= int(num[i+1]))
    return ans


def solution(left: int, right: int) -> int:
    counter = 0
    for number in range(left, right+1, 1):
        if is_six_digit(number) and is_within(number, left, right) \
                and two_adj(number) and never_decrease(number):
            counter += 1
    return counter


number = 111111
assert (is_six_digit(number) and two_adj(
    number) and never_decrease(number)) == True
number = 223450
assert (is_six_digit(number) and two_adj(
    number) and never_decrease(number)) == False

number = 123789
assert (is_six_digit(number) and two_adj(
    number) and never_decrease(number)) == False


# print(solution(359282, 820401))

# Part 2
def only_two_adj(number: int) -> bool:
    counts = Counter(str(number))
    return any([v == 2 for v in counts.values()])


def solution2(left: int, right: int) -> int:
    counter = 0
    for number in range(left, right+1, 1):
        if is_six_digit(number) and is_within(number, left, right) \
                and only_two_adj(number) and never_decrease(number):
            counter += 1
    return counter


number = 112233
assert (is_six_digit(number) and only_two_adj(
    number) and never_decrease(number)) == True

print(solution2(359282, 820401))
