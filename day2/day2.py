from typing import List


def add(a: int, b: int) -> int:
    return a+b


def mult(a: int, b: int) -> int:
    return a*b


ops = {1: add, 2: mult}

with open('input.txt') as f:
    data = [int(i) for i in f.read().split(',')]

data[1] = 12
data[2] = 2


def solution(data: List[int] = [1, 0, 0, 0, 99]):
    for i in range(0, len(data), 4):
        intcode = data[i]
        error = f"Got intcode {intcode}, i={i}, but accept only 1, 2, 99"
        assert intcode in [1, 2, 99], error
        if intcode != 99:
            arg1_pos = data[i+1]
            arg2_pos = data[i+2]
            out_pos = data[i+3]
            data[out_pos] = ops[intcode](data[arg1_pos], data[arg2_pos])
        else:
            return data
    return data


assert solution([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert solution([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert solution([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert solution([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

print(solution(data))
