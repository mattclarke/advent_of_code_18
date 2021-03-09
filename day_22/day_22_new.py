# Input data
from enum import Enum

DEPTH = 11394
TARGET = (7, 701)
EXTRA = 40

# Example => part 1 = 114, part 2 = 45
# DEPTH = 510
# TARGET = (10, 10)
# EXTRA = 10

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
class Equip(Enum):
    TORCH = 0
    CLIMB = 1
    NEITHER = 2


def can_switch_to(terrain):
    if terrain == 0:
        # Rocky
        return {Equip.CLIMB, Equip.TORCH}
    if terrain == 1:
        # Wet
        return {Equip.CLIMB, Equip.NEITHER}
    if terrain == 2:
        # Narrow
        return {Equip.TORCH, Equip.NEITHER}


def can_enter(terrain, equipped):
    if terrain == 0 and equipped == Equip.NEITHER:
        # Rocky .
        return False
    if terrain == 1 and equipped == Equip.TORCH:
        # Wet =
        return False
    if terrain == 2 and equipped == Equip.CLIMB:
        # Narrow |
        return False
    return True


cost_to_change = 7
queue = [((0, 0), Equip.TORCH, 0)]
distances = {
}

RESULTS = []


while queue:
    position, equipped, dist = queue.pop(0)
    print(position)
    if position == TARGET:
        if equipped != Equip.TORCH:
            dist += cost_to_change
        RESULTS.append(dist)
        continue

    if (position, equipped) in distances:
        if distances[(position, equipped)] <= dist:
            # Back-tracking
            continue
    distances[(position, equipped)] = dist

    if position not in erosion_levels:
        # raise Exception("bounds")
        continue

    curr_el = erosion_levels[position] % 3

    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        npos = (position[0] + x, position[1] + y)
        if npos[0] < 0 or npos[1] < 0:
            # Out of bounds
            continue
        if npos not in erosion_levels:
            # raise Exception("bounds")
            continue
        el = erosion_levels[npos] % 3
        if can_enter(el, equipped):
            queue.append((npos, equipped, dist + 1))
        else:
            options = can_switch_to(el)
            options = options.intersection(can_switch_to(curr_el))
            for option in options:
                queue.append((npos, option, dist + cost_to_change + 1))

# 969
print(min(RESULTS))
