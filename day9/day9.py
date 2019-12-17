"""Solution to day 9."""

from typing import List

Program = List[int]
Input = List[int]


class IntcodeComputer:
    """Full Intcode Computer."""

    def __init__(self, program: Program, debug: bool = False):
        """Constructor."""
        self.program = program[:] + [0]*3000
        self.idx = 0
        self.relative_base = 0
        self.input = []
        self.debug = debug

    def get_instruction(self, instr: int):
        """Parse the code and the mode."""
        out = str(instr)
        if len(out) <= 4:
            out = ''.join('0' for _ in range(5 - len(out))) + out
        code = int(out[-2:])
        mode3, mode2, mode1 = [int(x) for x in out[:-2]]
        return code, mode1, mode2, mode3

    def get_location(self, mode: int, idx: int):
        """Return the write location."""
        if mode == 0:
            return self.program[idx]
        elif mode == 2:
            return self.relative_base + self.program[idx]

    def get_param(self, mode: int, idx: int):
        """Retrieve parameter."""
        if self.debug:
            print(f"mode: {mode} at idx: {idx}")
        if mode == 0:  # position mode: the parameter is list index
            if self.program[idx] > len(self.program):
                raise ValueError(f"wrong index: {self.program[idx]} at {idx}")
            return self.program[self.program[idx]]
        elif mode == 1:
            return self.program[idx]
        elif mode == 2:
            return self.program[self.relative_base + self.program[idx]]
        else:
            raise ValueError(f"unknown mode {mode}")

    def run(self, inputs: Input) -> List[int]:
        """Run the intcode program."""
        self.input.extend(inputs)
        while self.idx < len(program):
            code, mode1, mode2, mode3 = self.get_instruction(
                self.program[self.idx])
            if code == 1:
                param1 = self.get_param(mode1, self.idx+1)
                param2 = self.get_param(mode2, self.idx+2)
                loc = self.get_location(mode3, self.idx+3)
                if self.debug:
                    print(
                        f"code:{code}, P1: {param1}, P2: {param2}, loc: {loc}")
                self.program[loc] = param1 + param2
                self.idx += 4
            elif code == 2:
                param1 = self.get_param(mode1, self.idx+1)
                param2 = self.get_param(mode2, self.idx+2)
                loc = self.get_location(mode3, self.idx+3)
                if self.debug:
                    print(
                        f"code:{code}, P1: {param1}, P2: {param2}, loc: {loc}")
                self.program[loc] = param1 * param2
                self.idx += 4
            elif code == 3:
                loc = self.get_location(mode1, self.idx+1)
                self.program[loc] = self.input.pop(0)
                self.idx += 2
            elif code == 4:
                out = self.get_param(mode1, self.idx+1)
                self.idx += 2
                return out
            elif code == 5:
                param1 = self.get_param(mode1, self.idx+1)
                param2 = self.get_param(mode2, self.idx+2)
                if self.debug:
                    print(f"code:{code}, P1: {param1}, P2: {param2}")
                if param1 != 0:
                    self.idx = param2
                else:
                    self.idx += 3
            elif code == 6:
                param1 = self.get_param(mode1, self.idx+1)
                param2 = self.get_param(mode2, self.idx+2)
                if self.debug:
                    print(f"code:{code}, P1: {param1},",
                          " P2: {param2}")
                if param1 == 0:
                    self.idx = param2
                else:
                    self.idx += 3
            elif code == 7:
                param1 = self.get_param(mode1, self.idx+1)
                param2 = self.get_param(mode2, self.idx+2)
                param3 = self.get_location(mode3, self.idx+3)
                if self.debug:
                    print(
                        f"code:{code}, P1: {param1},",
                        " P2: {param2}, P3: {param3}")
                if param1 < param2:
                    self.program[param3] = 1
                else:
                    self.program[param3] = 0
                self.idx += 4
            elif code == 8:
                param1 = self.get_param(mode1, self.idx+1)
                param2 = self.get_param(mode2, self.idx+2)
                param3 = self.get_location(mode3, self.idx+3)
                if self.debug:
                    print(
                        f"code:{code}, P1: {param1}, ",
                        "P2: {param2}, P3: {param3}")
                if param1 == param2:
                    self.program[param3] = 1
                else:
                    self.program[param3] = 0
                self.idx += 4
            elif code == 9:
                param1 = self.get_param(mode1, self.idx+1)
                self.relative_base += param1
                self.idx += 2
            elif self.program[self.idx] == 99:
                return None


with open("input.txt") as f:
    data = f.readlines()

program = [int(x) for x in data[0].split(',')]


def run(program: Program, inputs: Input = []):
    """Run the main program."""
    computer = IntcodeComputer(program, debug=False)
    temp = 0
    outputs = []
    while temp is not None:
        temp = computer.run(inputs)
        inputs = []
        if temp is not None:
            outputs.append(temp)
    return outputs


# print(run(program=[109, 1, 204, -1, 1001, 100, 1, 100,
#                    1008, 100, 16, 101, 1006, 101, 0, 99]))
# print(run(program=[1102, 34915192, 34915192, 7, 4, 7, 99, 0]))
# print(run(program=[104, 1125899906842624, 99]))
print("Test run", run(program, [1]))
print("Full run", run(program, [2]))
