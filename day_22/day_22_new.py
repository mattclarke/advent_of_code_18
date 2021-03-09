# Input data
DEPTH = 11394
TARGET = (7, 701)
EXTRA = 10

# Example = 114
DEPTH = 510
TARGET = (10, 10)

MODULO = 20183

erosion_levels = {

}

# Calculate erosion levels
for y in range(0, TARGET[1] + EXTRA):
    for x in range(0, TARGET[0] + EXTRA):
        if (x, y) == TARGET:
            gi = 0
        elif x == 0:
            gi = y * 48271
        elif y == 0:
            gi = x * 16807
        else:
            gi = erosion_levels[(x - 1, y)] * erosion_levels[(x, y - 1)]
        el = (gi + DEPTH) % MODULO
        erosion_levels[(x, y)] = el


def print_layout():
    for y in range(TARGET[1] + EXTRA):
        line = []
        for x in range(TARGET[0] + EXTRA):
            if (x, y) == (0,0):
                line.append("M")
                continue
            if (x,y) == TARGET:
                line.append("T")
                continue

            el = erosion_levels.get((x, y), 0)
            t = el % 3
            if t == 0:
                line.append(".")
            elif t == 1:
                line.append("=")
            elif t == 2:
                line.append("|")
            else:
                assert False
        print("".join(line))


def calc_risk():
    total = 0
    for y in range(TARGET[1]+1):
        for x in range(TARGET[0]+1):
            el = erosion_levels.get((x, y), 0)
            total += el % 3
    return total


# 5637
print(f"Part 1: {calc_risk()}")

# Part 2
