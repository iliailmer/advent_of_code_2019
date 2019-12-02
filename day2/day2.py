from typing import List


def add(a: int, b: int) -> int:
    return a+b


def mult(a: int, b: int) -> int:
    return a*b


ops = {1: add, 2: mult}

with open('input.txt') as f:
    data = [int(i) for i in f.read().split(',')]

data[1] = 12  # noun
data[2] = 2  # verb


def solution(data: List[int] = [1, 0, 0, 0, 99]) -> List[int]:
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

print(solution(data)[0])

for i in range(100):
    for j in range(100):
        INPUT = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,5,19,23,1,23,6,27,1,5,27,31,1,31,6,35,1,9,35,39,2,10,39,43,1,43,6,47,2,6,47,51,1,5,51,55,1,55,13,59,1,59,10,63,2,10,63,67,1,9,67,71,2,6,71,75,1,5,75,79,2,79,13,83,1,83,5,87,1,87,9,91,1,5,91,95,1,5,95,99,1,99,13,103,1,10,103,107,1,107,9,111,1,6,111,115,2,115,13,119,1,10,119,123,2,123,6,127,1,5,127,131,1,5,131,135,1,135,6,139,2,139,10,143,2,143,9,147,1,147,6,151,1,151,13,155,2,155,9,159,1,6,159,163,1,5,163,167,1,5,167,171,1,10,171,175,1,13,175,179,1,179,2,183,1,9,183,0,99,2,14,0,0]
        INPUT[1] = i
        INPUT[2] = j
        if (solution(INPUT)[0] == 19690720):
            print(i, j, 100*i+j)