from typing import List


def add(a: int, b: int) -> int:
    return a + b


def mult(a: int, b: int) -> int:
    return a * b


def input_(val: int, data: List[int], a: int) -> List[int]:
    data[a] = val
    return data


ops = {1: add, 2: mult, 3: input_, 4: print}


def get_instruction(instr: int):
    out = str(instr)
    if len(out) <= 4:
        out = ''.join('0' for _ in range(5 - len(out))) + out
    code = int(out[-2:])
    mode3, mode2, mode1 = [int(x) for x in out[:-2]]
    return code, mode1, mode2, mode3


def apply_program(val: int, program: List[int] = [1002, 4, 3, 4, 33]):
    i = 0
    out: List[int] = []
    while program[i] != 99:
        code, mode1, mode2, mode3 = get_instruction(program[i])
        if code == 1:
            if mode1 == 0:  # position mode: the parameter is list index
                param1 = program[program[i + 1]]
            else:
                param1 = program[i + 1]
            if mode2 == 0:
                param2 = program[program[i + 2]]
            else:
                param2 = program[i + 2]
            if mode3 == 0:
                program[program[i + 3]] = add(param1, param2)
                print(f"adding {param1} + {param2} at {program[i+3]}")
            else:
                program[i + 3] = add(param1, param2)
                print(f"adding {param1} + {param2} at {i+3}")
            i += 4
        elif code == 2:
            if mode1 == 0:  # position mode: the parameter is list index
                param1 = program[program[i + 1]]
            else:
                param1 = program[i + 1]
            if mode2 == 0:
                param2 = program[program[i + 2]]
            else:
                param2 = program[i + 2]
            if mode3 == 0:
                program[program[i + 3]] = mult(param1, param2)
                print(
                    f"multipluying {param1} + {param2} at {program[i+3]}")
            else:
                program[i + 3] = mult(param1, param2)
                print(
                    f"multipluying {param1} + {param2} at {program[i+3]}")
            i += 4
        elif code == 3:
            program[program[i + 1]] = val
            i += 2
            print(f"inputting {val} to {program[i+1]}")
        elif code == 4:
            if mode1 == 0:
                out.append(program[program[i + 1]])
                print(f"outputting {program[program[i+1]]}")
            else:
                out.append(program[i + 1])
                print(f"outputting {program[i+1]}")
            i += 2
        elif code == 5:
            if mode1 == 0:
                param1 = program[program[i + 1]]
            else:
                param1 = program[i + 1]
            if mode2 == 0:
                param2 = program[program[i + 2]]
            else:
                param2 = program[i + 2]
            if param1 != 0:
                i = param2
            else:
                i += 3
        elif code == 6:
            if mode1 == 0:
                param1 = program[program[i + 1]]
            else:
                param1 = program[i + 1]
            if mode2 == 0:
                param2 = program[program[i + 2]]
            else:
                param2 = program[i + 2]
            if param1 == 0:
                i = param2
            else:
                i += 3
        elif code == 7:
            if mode1 == 0:
                param1 = program[program[i + 1]]
            else:
                param1 = program[i + 1]
            if mode2 == 0:
                param2 = program[program[i + 2]]
            else:
                param2 = program[i + 2]
            # parameters that are written are never in immediate mode
            param3 = program[i + 3]
            if param1 < param2:
                program[param3] = 1
            else:
                program[param3] = 0
            i += 4
        elif code == 8:
            if mode1 == 0:
                param1 = program[program[i + 1]]
            else:
                param1 = program[i + 1]
            if mode2 == 0:
                param2 = program[program[i + 2]]
            else:
                param2 = program[i + 2]
            # parameters that are written are never in immediate mode
            param3 = program[i + 3]
            if param1 == param2:
                program[param3] = 1
            else:
                program[param3] = 0
            i += 4
    return out


data = [
    3,
    225,
    1,
    225,
    6,
    6,
    1100,
    1,
    238,
    225,
    104,
    0,
    1101,
    86,
    8,
    225,
    1101,
    82,
    69,
    225,
    101,
    36,
    65,
    224,
    1001,
    224,
    -106,
    224,
    4,
    224,
    1002,
    223,
    8,
    223,
    1001,
    224,
    5,
    224,
    1,
    223,
    224,
    223,
    102,
    52,
    148,
    224,
    101,
    -1144,
    224,
    224,
    4,
    224,
    1002,
    223,
    8,
    223,
    101,
    1,
    224,
    224,
    1,
    224,
    223,
    223,
    1102,
    70,
    45,
    225,
    1002,
    143,
    48,
    224,
    1001,
    224,
    -1344,
    224,
    4,
    224,
    102,
    8,
    223,
    223,
    101,
    7,
    224,
    224,
    1,
    223,
    224,
    223,
    1101,
    69,
    75,
    225,
    1001,
    18,
    85,
    224,
    1001,
    224,
    -154,
    224,
    4,
    224,
    102,
    8,
    223,
    223,
    101,
    2,
    224,
    224,
    1,
    224,
    223,
    223,
    1101,
    15,
    59,
    225,
    1102,
    67,
    42,
    224,
    101,
    -2814,
    224,
    224,
    4,
    224,
    1002,
    223,
    8,
    223,
    101,
    3,
    224,
    224,
    1,
    223,
    224,
    223,
    1101,
    28,
    63,
    225,
    1101,
    45,
    22,
    225,
    1101,
    90,
    16,
    225,
    2,
    152,
    92,
    224,
    1001,
    224,
    -1200,
    224,
    4,
    224,
    102,
    8,
    223,
    223,
    101,
    7,
    224,
    224,
    1,
    223,
    224,
    223,
    1101,
    45,
    28,
    224,
    1001,
    224,
    -73,
    224,
    4,
    224,
    1002,
    223,
    8,
    223,
    101,
    7,
    224,
    224,
    1,
    224,
    223,
    223,
    1,
    14,
    118,
    224,
    101,
    -67,
    224,
    224,
    4,
    224,
    1002,
    223,
    8,
    223,
    1001,
    224,
    2,
    224,
    1,
    223,
    224,
    223,
    4,
    223,
    99,
    0,
    0,
    0,
    677,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1105,
    0,
    99999,
    1105,
    227,
    247,
    1105,
    1,
    99999,
    1005,
    227,
    99999,
    1005,
    0,
    256,
    1105,
    1,
    99999,
    1106,
    227,
    99999,
    1106,
    0,
    265,
    1105,
    1,
    99999,
    1006,
    0,
    99999,
    1006,
    227,
    274,
    1105,
    1,
    99999,
    1105,
    1,
    280,
    1105,
    1,
    99999,
    1,
    225,
    225,
    225,
    1101,
    294,
    0,
    0,
    105,
    1,
    0,
    1105,
    1,
    99999,
    1106,
    0,
    300,
    1105,
    1,
    99999,
    1,
    225,
    225,
    225,
    1101,
    314,
    0,
    0,
    106,
    0,
    0,
    1105,
    1,
    99999,
    7,
    677,
    677,
    224,
    102,
    2,
    223,
    223,
    1005,
    224,
    329,
    1001,
    223,
    1,
    223,
    1008,
    226,
    226,
    224,
    1002,
    223,
    2,
    223,
    1005,
    224,
    344,
    1001,
    223,
    1,
    223,
    1107,
    677,
    226,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    359,
    1001,
    223,
    1,
    223,
    107,
    677,
    677,
    224,
    102,
    2,
    223,
    223,
    1005,
    224,
    374,
    101,
    1,
    223,
    223,
    1108,
    677,
    226,
    224,
    102,
    2,
    223,
    223,
    1005,
    224,
    389,
    1001,
    223,
    1,
    223,
    1007,
    677,
    677,
    224,
    1002,
    223,
    2,
    223,
    1005,
    224,
    404,
    101,
    1,
    223,
    223,
    1008,
    677,
    226,
    224,
    102,
    2,
    223,
    223,
    1005,
    224,
    419,
    101,
    1,
    223,
    223,
    1108,
    226,
    677,
    224,
    102,
    2,
    223,
    223,
    1006,
    224,
    434,
    1001,
    223,
    1,
    223,
    8,
    677,
    226,
    224,
    1002,
    223,
    2,
    223,
    1005,
    224,
    449,
    101,
    1,
    223,
    223,
    1008,
    677,
    677,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    464,
    1001,
    223,
    1,
    223,
    1108,
    226,
    226,
    224,
    1002,
    223,
    2,
    223,
    1005,
    224,
    479,
    1001,
    223,
    1,
    223,
    1007,
    226,
    677,
    224,
    102,
    2,
    223,
    223,
    1005,
    224,
    494,
    1001,
    223,
    1,
    223,
    1007,
    226,
    226,
    224,
    102,
    2,
    223,
    223,
    1005,
    224,
    509,
    101,
    1,
    223,
    223,
    107,
    677,
    226,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    524,
    1001,
    223,
    1,
    223,
    108,
    677,
    677,
    224,
    102,
    2,
    223,
    223,
    1006,
    224,
    539,
    101,
    1,
    223,
    223,
    7,
    677,
    226,
    224,
    102,
    2,
    223,
    223,
    1006,
    224,
    554,
    1001,
    223,
    1,
    223,
    1107,
    226,
    677,
    224,
    102,
    2,
    223,
    223,
    1005,
    224,
    569,
    101,
    1,
    223,
    223,
    108,
    677,
    226,
    224,
    1002,
    223,
    2,
    223,
    1006,
    224,
    584,
    101,
    1,
    223,
    223,
    108,
    226,
    226,
    224,
    102,
    2,
    223,
    223,
    1006,
    224,
    599,
    1001,
    223,
    1,
    223,
    1107,
    226,
    226,
    224,
    102,
    2,
    223,
    223,
    1006,
    224,
    614,
    1001,
    223,
    1,
    223,
    8,
    226,
    677,
    224,
    102,
    2,
    223,
    223,
    1006,
    224,
    629,
    1001,
    223,
    1,
    223,
    107,
    226,
    226,
    224,
    102,
    2,
    223,
    223,
    1005,
    224,
    644,
    101,
    1,
    223,
    223,
    8,
    226,
    226,
    224,
    102,
    2,
    223,
    223,
    1006,
    224,
    659,
    101,
    1,
    223,
    223,
    7,
    226,
    677,
    224,
    102,
    2,
    223,
    223,
    1005,
    224,
    674,
    101,
    1,
    223,
    223,
    4,
    223,
    99,
    226]

print(apply_program(5, data))
