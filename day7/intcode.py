from typing import List


def get_instruction(instr: int):
    """Parses the code and the mode."""
    out = str(instr)
    if len(out) <= 4:
        out = ''.join('0' for _ in range(5 - len(out))) + out
    code = int(out[-2:])
    mode3, mode2, mode1 = [int(x) for x in out[:-2]]
    return code, mode1, mode2, mode3


def run(phase_signal: List[int],
        program: List[int] = [1002, 4, 3, 4, 33]) -> List[int]:
    """Runs the intcode program.
       :param:
    """
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
                program[program[i + 3]] = param1 + param2
                # print(f"adding {param1} + {param2} at {program[i+3]}")
            else:
                program[i + 3] = param1 + param2
                # print(f"adding {param1} + {param2} at {i+3}")
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
                program[program[i + 3]] = param1 * param2
                # print(
                # f"multipluying {param1} + {param2} at
                # {program[i+3]}")
            else:
                program[i + 3] = param1 * param2
                # print(
                # f"multipluying {param1} + {param2} at
                # {program[i+3]}")
            i += 4
        elif code == 3:
            print(phase_signal)
            program[program[i + 1]] = phase_signal[0]
            phase_signal = phase_signal[1:]
            i += 2
        elif code == 4:
            if mode1 == 0:
                out.append(program[program[i + 1]])
            else:
                out.append(program[i + 1])
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


def run_all(phases: List[int], program: List[int]) -> int:
    signal = 0
    for phase in phases:
        signal, = run([phase, signal], program)
    return signal
