import re

real_data = """
#ip 5
addi 5 16 5
seti 1 0 3
seti 1 2 2
mulr 3 2 4
eqrr 4 1 4
addr 4 5 5
addi 5 1 5
addr 3 0 0
addi 2 1 2
gtrr 2 1 4
addr 5 4 5
seti 2 7 5
addi 3 1 3
gtrr 3 1 4
addr 4 5 5
seti 1 3 5
mulr 5 5 5
addi 1 2 1
mulr 1 1 1
mulr 5 1 1
muli 1 11 1
addi 4 7 4
mulr 4 5 4
addi 4 20 4
addr 1 4 1
addr 5 0 5
seti 0 4 5
setr 5 9 4
mulr 4 5 4
addr 5 4 4
mulr 5 4 4
muli 4 14 4
mulr 4 5 4
addr 1 4 1
seti 0 2 0
seti 0 5 5
"""

test_data = """
#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5
"""


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
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtir": gtir,
    "gtri": gtri,
    "gtrr": gtrr,
    "eqir": eqir,
    "eqri": eqri,
    "eqrr": eqrr,
}

cmds = []

for line in real_data.splitlines():
    if not line:
        continue
    ipm = re.match(r"(#ip) (\d+)", line)
    om = re.match(r"(\w+) (\d+) (\d+) (\d+)", line)
    if ipm:
        cmds.append((ipm.groups()[0], int(ipm.groups()[1])))
    elif om:
        cmds.append(
            (
                om.groups()[0],
                int(om.groups()[1]),
                int(om.groups()[2]),
                int(om.groups()[3]),
            )
        )
    else:
        raise Exception("Regex fail")


def print_registers(ip, before, cmd, after):
    line = f"ip={ip} [{before[0]}, {before[1]}, {before[2]}, {before[3]}, {before[4]}, {before[5]}]"
    line += f" {cmd[0]} {cmd[1]} {cmd[2]} {cmd[3]} "
    line += f"[{after[0]}, {after[1]}, {after[2]}, {after[3]}, {after[4]}, {after[5]}]"
    print(line)


print(cmds)

# For part 1 = 1836
registers = [0, 0, 0, 0, 0, 0]
ip = 0
first = cmds.pop(0)
if first[0] != "#ip":
    raise Exception("oops")

ip_reg = first[1]

while True:
    c = cmds[ip]

    # Update ip register to ip value
    registers[ip_reg] = ip
    before = registers[:]

    # Do the operation
    ops[c[0]](registers, c[1], c[2], c[3])

    print_registers(ip, before, c, registers)

    # Update ip value
    ip = registers[ip_reg]
    ip += 1

    if ip >= len(cmds):
        break

# Part 2
# Quicker to read the source code: it is essentially finding the factors of a big number
# then summing them to together.
# 18992556
