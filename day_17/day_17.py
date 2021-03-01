import re
from collections import deque

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

test_data_1 = """
x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
"""

test_data_2 = """
y=7, x=495..501
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
"""

test_data_3 = """
y=7, x=500..501
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
"""

test_data_4 = """
y=7, x=500..501
y=10, x=500..501
y=11, x=500..501
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504
"""

raw_data = PUZZLE_INPUT

x_min = float("inf")
x_max = 0
y_min = float("inf")
y_max = 0

# Quick scan to find mins and maxs
for line in raw_data.splitlines():
    if not line:
        continue
    m1 = re.match(r"x=(\d+), y=(\d+)\.\.(\d+)", line)
    m2 = re.match(r"y=(\d+), x=(\d+)\.\.(\d+)", line)
    if m1:
        x_min = min(int(m1.groups()[0]), x_min)
        x_max = max(int(m1.groups()[0]), x_max)
        y_min = min(int(m1.groups()[1]), y_min)
        y_max = max(int(m1.groups()[2]), y_max)
    elif m2:
        y_min = min(int(m2.groups()[0]), y_min)
        y_max = max(int(m2.groups()[0]), y_max)
        x_min = min(int(m2.groups()[1]), x_min)
        x_max = max(int(m2.groups()[2]), x_max)
    else:
        raise Exception("Regex fail!")

x_min -= 1
x_max += 2
# print(x_min, x_max, y_min, y_max)

board = [[None for y in range(y_max - y_min + 2)] for x in range(x_max - x_min)]


# Add the spring
board[500 - x_min][0] = "+"

# Build the board
for line in raw_data.splitlines():
    if not line:
        continue
    m1 = re.match(r"x=(\d+), y=(\d+)\.\.(\d+)", line)
    m2 = re.match(r"y=(\d+), x=(\d+)\.\.(\d+)", line)
    if m1:
        for y in range(int(m1.groups()[1]), int(m1.groups()[2]) + 1):
            x = int(m1.groups()[0]) - x_min
            board[x][y - y_min + 1] = "#"
    elif m2:
        for x in range(int(m2.groups()[1]), int(m2.groups()[2])):
            y = int(m2.groups()[0]) - y_min + 1
            board[x - x_min][y] = "#"
    else:
        raise Exception("Regex fail!")


def print_board(board, y_pos):
    print("")
    min_y = y_pos - 20 if y_pos > 20 else 0
    max_y = y_pos + 20 if y_pos + 20 < len(board[0]) - 1 else len(board[0]) - 1

    for y in range(min_y, max_y):
        line = "{}".format(y).ljust(5)
        for x in range(len(board)):
            if board[x][y] is not None:
                line += board[x][y]
            else:
                line += "."
        print(line)


def pour(board, x, y):
    while board[x][y + 1] != "#":
        # Hit something already overflowing?
        if board[x][y + 1] == "|":
            return None, None
        board[x][y + 1] = "|"
        y += 1
        if y == len(board[0]) - 1:
            return None, None
    board[x][y] = "~"
    return x, y


def find_left(board, x, y):
    while board[x][y] != "#":
        # Is there nothing "solid" underneath?
        if board[x][y + 1] is None or board[x][y + 1] == "|":
            return x, True
        x -= 1
    x += 1
    return x, False


def find_right(board, x, y):
    while board[x][y] != "#":
        # Is there nothing beneath?
        if board[x][y + 1] is None or board[x][y + 1] == "|":
            return x, True
        x += 1
    x -= 1
    return x, False


def do_fill(board, pos_x, pos_y, overflows):
    # TODO: Check for ledges
    # Find edges
    # Left first then right
    l_edge = None
    r_edge = None

    while True:
        l_edge, l_overflow = find_left(board, pos_x, pos_y)

        r_edge, r_overflow = find_right(board, pos_x, pos_y)

        # Fill
        for i in range(l_edge, r_edge + 1):
            if l_overflow or r_overflow:
                board[i][pos_y] = "|"
            else:
                board[i][pos_y] = "~"

        # print_board(board, pos_y)

        # Resolve overflow
        if l_overflow or r_overflow:
            if l_overflow:
                overflows.append((l_edge, pos_y))
            if r_overflow:
                overflows.append((r_edge, pos_y))
            break

        pos_y -= 1


def count_water(board, water=["~", "|"]):
    count = 0
    for y in range(len(board[0])):
        for x in range(len(board)):
            if board[x][y] in water:
                count += 1
    return count


# Part 1
# print_board(board, 0)
# Start by filling from spring
overflows = [(500 - x_min, 0)]
fill_points = []

while fill_points or overflows:
    if overflows:
        of = overflows.pop(0)
        pos_x, pos_y = pour(board, *of)
        if pos_x and pos_y:
            fill_points.append((pos_x, pos_y))
            # print_board(board, pos_y)

    # Start filling
    if fill_points:
        fp = fill_points.pop(0)
        do_fill(board, *fp, overflows)
        # print_board(board, pos_y)

# 27206
print(f"Part 1: {count_water(board)}")

# Part 2 = 21787
print(f"Part 2: {count_water(board, ['~'])}")
