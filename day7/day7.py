"""Solution to day 7."""

from intcode import run_all
from typing import List
from itertools import permutations
phase_sequence = permutations([4, 3, 2, 1, 0])

# with open("input.txt") as f:
#     program = [int(x) for x in f.read().split(',')]

# signal = 0

# for phases in phase_sequence:
#     signal = max(signal, run_all(phases, program=program))


class Amplifier:
    """Amplifier class."""

    def __init__(self, phase: int, program: List[int]) -> None:
        """Amplifier class.

        :param phase: (int) phase
        :param signal: (int), signal
        """
        self.input = [phase]
        self.program = program[:]
        self.i = 0  # position, we cannot restart the amplifier

    def get_instruction(self, instr: int):
        """Parse the code and the mode."""
        out = str(instr)
        if len(out) <= 4:
            out = ''.join('0' for _ in range(5 - len(out))) + out
        code = int(out[-2:])
        mode3, mode2, mode1 = [int(x) for x in out[:-2]]
        return code, mode1, mode2, mode3

    def run(self, input) -> int:
        """Run the intcode program.

        :param phase_signal: input pair of phase and signal
        """
        self.input.append(input)
        out = 0
        while True:
            code, mode1, mode2, mode3 = self.get_instruction(
                self.program[self.i])
            if code == 99:
                return None
            if code == 1:
                if mode1 == 0:  # position mode: the parameter is list index
                    param1 = self.program[self.program[self.i + 1]]
                else:
                    param1 = self.program[self.i + 1]
                if mode2 == 0:
                    param2 = self.program[self.program[self.i + 2]]
                else:
                    param2 = self.program[self.i + 2]
                if mode3 == 0:
                    self.program[self.program[self.i + 3]] = param1 + param2
                    # print(f"adding {param1} + {param2} at {program[i+3]}")
                else:
                    self.program[self.i + 3] = param1 + param2
                    # print(f"adding {param1} + {param2} at {i+3}")
                self.i += 4
            elif code == 2:
                if mode1 == 0:  # position mode: the parameter is list index
                    param1 = self.program[self.program[self.i + 1]]
                else:
                    param1 = self.program[self.i + 1]
                if mode2 == 0:
                    param2 = self.program[self.program[self.i + 2]]
                else:
                    param2 = self.program[self.i + 2]
                if mode3 == 0:
                    self.program[self.program[self.i + 3]] = param1 * param2
                else:
                    self.program[self.i + 3] = param1 * param2
                self.i += 4
            elif code == 3:
                self.program[self.program[self.i + 1]] = self.input[0]
                self.input = self.input[1:]
                self.i += 2
            elif code == 4:
                if mode1 == 0:
                    out = (self.program[self.program[self.i + 1]])
                else:
                    out = (self.program[self.i + 1])
                self.i += 2
                return out
            elif code == 5:
                if mode1 == 0:
                    param1 = self.program[self.program[self.i + 1]]
                else:
                    param1 = self.program[self.i + 1]
                if mode2 == 0:
                    param2 = self.program[self.program[self.i + 2]]
                else:
                    param2 = self.program[self.i + 2]
                if param1 != 0:
                    self.i = param2
                else:
                    self.i += 3
            elif code == 6:
                if mode1 == 0:
                    param1 = self.program[self.program[self.i + 1]]
                else:
                    param1 = self.program[self.i + 1]
                if mode2 == 0:
                    param2 = self.program[self.program[self.i + 2]]
                else:
                    param2 = self.program[self.i + 2]
                if param1 == 0:
                    self.i = param2
                else:
                    self.i += 3
            elif code == 7:
                if mode1 == 0:
                    param1 = self.program[self.program[self.i + 1]]
                else:
                    param1 = self.program[self.i + 1]
                if mode2 == 0:
                    param2 = self.program[self.program[self.i + 2]]
                else:
                    param2 = self.program[self.i + 2]
                # parameters that are written are never in immediate mode
                param3 = self.program[self.i + 3]
                if param1 < param2:
                    self.program[param3] = 1
                else:
                    self.program[param3] = 0
                self.i += 4
            elif code == 8:
                if mode1 == 0:
                    param1 = self.program[self.program[self.i + 1]]
                else:
                    param1 = self.program[self.i + 1]
                if mode2 == 0:
                    param2 = self.program[self.program[self.i + 2]]
                else:
                    param2 = self.program[self.i + 2]
                # parameters that are written are never in immediate mode
                param3 = self.program[self.i + 3]
                if param1 == param2:
                    self.program[param3] = 1
                else:
                    self.program[param3] = 0
                self.i += 4

        def __repr__(self):
            return f"{self.input}"


phase_sequence = [4, 3, 2, 1, 0]
program = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]


def part1(phase: List[int], program: List[int]):
    signal = 0
    amplifiers = [Amplifier(phase, program) for phase in phase_sequence]
    for amp in amplifiers:
        signal = max(amp.run(signal), signal)
    return signal


assert part1(phase_sequence, program) == 43210  # the code works

phase_sequence = [9, 8, 7, 6, 5]
program = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
           27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]


def run_amplifier(phase_sequence: List[int], program: List[int]):
    amplifiers = [Amplifier(phase, program) for phase in phase_sequence]
    amp_idx = 0
    num_finished = 0
    n = len(amplifiers)
    signal = 0
    output = None
    while num_finished < n:
        signal = amplifiers[amp_idx].run(signal)
        if signal is None:
            num_finished += 1
        else:
            output = signal
        amp_idx = (amp_idx + 1) % n
    return output


def part2(program: List[int]):
    perms = permutations([5, 6, 7, 8, 9])
    out = 0
    for perm in perms:
        out = max(out, run_amplifier(perm, program))
    return out


with open("input.txt") as f:
    program = [int(x) for x in f.read().split(',')]


print(part2(program))
