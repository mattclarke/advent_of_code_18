import re

test_data = """
#ip 3
seti 123 0 1
bani 1 456 1
eqri 1 72 1
addr 1 3 3
seti 0 0 3
seti 0 0 1
bori 1 65536 2
seti 10605201 9 1
bani 2 255 5
addr 1 5 1
bani 1 16777215 1
muli 1 65899 1
bani 1 16777215 1
gtir 256 2 5
addr 5 3 3
addi 3 1 3
seti 27 3 3
seti 0 3 5
addi 5 1 4
muli 4 256 4
gtrr 4 2 4
addr 4 3 3
addi 3 1 3
seti 25 3 3
addi 5 1 5
seti 17 5 3
setr 5 5 2
seti 7 6 3
eqrr 1 0 5
addr 5 3 3
seti 5 8 3
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

for line in test_data.splitlines():
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

registers = [0, 0, 0, 0, 0, 0]
ip = 0
first = cmds.pop(0)
if first[0] != "#ip":
    raise Exception("oops")

ip_reg = first[1]
count = 0
two = registers[2]

counts = set()

while True:
    c = cmds[ip]

    # Update ip register to ip value
    registers[ip_reg] = ip
    before = registers[:]

    if ip == 28:
        # TODO: Somehow check for repeating register
        if registers[1] in counts:
            print("Repeating")
        counts.add(registers[1])
        print(registers[1])


    # if two != registers[2]:
    #     print("here")
    #     two =registers[2]

    # Do the operation
    ops[c[0]](registers, c[1], c[2], c[3])
    count += 1

    # print_registers(ip, before, c, registers)

    # Update ip value
    ip = registers[ip_reg]
    ip += 1

    if ip >= len(cmds):
        break

print(count)