import re


with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

samples, program = PUZZLE_INPUT.split("\n\n\n\n")


def addr(registers, a, b, c):
    registers[c] = registers[a] + registers[b]


def addi(registers, a, b, c):
    registers[c] = registers[a] + b


def mulr(registers, a, b, c):
    registers[c] = registers[a] * registers[b]


def muli(registers, a, b, c):
    registers[c] = registers[a] * b


def banr(registers, a, b, c):
    registers[c] = registers[a] & registers[b]


def bani(registers, a, b, c):
    registers[c] = registers[a] & b


def borr(registers, a, b, c):
    registers[c] = registers[a] | registers[b]


def bori(registers, a, b, c):
    registers[c] = registers[a] | b


def setr(registers, a, b, c):
    registers[c] = registers[a]


def seti(registers, a, b, c):
    registers[c] = a


def gtir(registers, a, b, c):
    registers[c] = 1 if a > registers[b] else 0


def gtri(registers, a, b, c):
    registers[c] = 1 if registers[a] > b else 0


def gtrr(registers, a, b, c):
    registers[c] = 1 if registers[a] > registers[b] else 0


def eqir(registers, a, b, c):
    registers[c] = 1 if a == registers[b] else 0


def eqri(registers, a, b, c):
    registers[c] = 1 if registers[a] == b else 0


def eqrr(registers, a, b, c):
    registers[c] = 1 if registers[a] == registers[b] else 0


ops = {
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr,
}


def try_ops(before, operation, after):
    valid = []
    for op in ops:
        code = before[:]
        op(code, operation[1], operation[2], operation[3])
        if code == after:
            valid.append(op)
            # print(op)
    return valid


before = None
operation = None
after = None
three_or_more = 0

# Part 2
opcodes = {}
for i in range(16):
    opcodes[i] = list(ops)

for line in samples.splitlines():
    if not line:
        continue
    bm = re.match(r"Before: \[(\d+), (\d+), (\d+), (\d+)\]", line)
    om = re.match(r"(\d+) (\d+) (\d+) (\d+)", line)
    am = re.match(r"After:  \[(\d+), (\d+), (\d+), (\d+)\]", line)
    if bm:
        before = [
            int(bm.groups()[0]),
            int(bm.groups()[1]),
            int(bm.groups()[2]),
            int(bm.groups()[3]),
        ]
        # print(before)

    if om:
        operation = [
            int(om.groups()[0]),
            int(om.groups()[1]),
            int(om.groups()[2]),
            int(om.groups()[3]),
        ]
        # print(operation)

    if am:
        after = [
            int(am.groups()[0]),
            int(am.groups()[1]),
            int(am.groups()[2]),
            int(am.groups()[3]),
        ]
        # print(after)
        valid = try_ops(before, operation, after)
        # Part 1
        if len(valid) >= 3:
            three_or_more += 1

        # Part 2
        to_remove = []
        for op in ops:
            if op not in valid:
                to_remove.append(op)
        for r in to_remove:
            if r in opcodes[operation[0]]:
                opcodes[operation[0]].remove(r)
        if len(opcodes[operation[0]]) == 1:
            # Remove it from others
            for n, v in opcodes.items():
                if n == operation[0]:
                    continue
                if opcodes[operation[0]][0] in v:
                    v.remove(opcodes[operation[0]][0])

# Part 1 = 567
print(f"Part 1: {three_or_more}")

# Part 2 - sanity check that all opcodes found
sanity = set()
for n, v in opcodes.items():
    if len(v) > 1:
        raise Exception("Too many")
    if v[0] in sanity:
        raise Exception("Duplicate")
    sanity.add(v[0])

prog_registers = [0, 0, 0, 0]

for line in program.splitlines():
    if not line:
        continue
    om = re.match(r"(\d+) (\d+) (\d+) (\d+)", line)
    operation = [
        int(om.groups()[0]),
        int(om.groups()[1]),
        int(om.groups()[2]),
        int(om.groups()[3]),
    ]
    opcodes[operation[0]][0](prog_registers, operation[1], operation[2], operation[3])

print(f"Part 2: {prog_registers[0]}")
