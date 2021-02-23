target = (10, 10)
depth = 510

# Real data
depth = 11394
target = (7, 701)

board = [[None for y in range(target[1] + 10)] for x in range(target[0] + 10)]


def calculate_index(x, y, board):
    if x == 0 and y == 0:
        return 0
    elif (x, y) == target:
        return 0
    elif y == 0:
        return x * 16807
    elif x == 0:
        return y * 48271
    else:
        return board[x - 1][y] * board[x][y - 1]


def calculate_level(gi):
    return (gi + depth) % 20183


def get_type(level):
    if level % 3 == 0:
        return "."
    elif level % 3 == 1:
        return "="
    elif level % 3 == 2:
        return "|"


def draw_board(board):
    total = 0
    for y in range(len(board[0])):
        line = ""
        for x in range(len(board)):
            if (x, y) == (0, 0):
                line += "M"
            elif (x, y) == target:
                line += "T"
            else:
                line += get_type(board[x][y])
            if x <= target[0] and y <= target[1]:
                total += board[x][y] % 3
        print(line)
    print(total)


def populate_board(board):
    for y in range(len(board[0])):
        for x in range(len(board)):
            index = calculate_index(x, y, board)
            level = calculate_level(index)
            board[x][y] = level
    return board


board = populate_board(board)
draw_board(board)

# Part 2
# if rocky must use gear (2) or torch (1)
# if wet must use gear or nothing (0)
# if narrow must use torch or nothing
# Each step takes 1
# Switching takes 7
# Starts with torch
# At target must switch to torch
NOTHING = 0
TORCH = 1
GEAR = 2

height = target[1] + 10
width = target[0] + 50

board = [[None for y in range(height)] for x in range(width)]
route_board = [[None for y in range(height)] for x in range(width)]

board = populate_board(board)
# Convert board to type
for y in range(height):
    for x in range(width):
        board[x][y] = get_type(board[x][y])

# for y in range(height):
#     line = ""
#     for x in range(width):
#         line += board[x][y]
#     print(line)


# Do a test run to get a "maximum"
master_route_board = [[[None, None] for y in range(height)] for x in range(width)]

equipped = TORCH
count = 0
x = 0
y = 0

# Move to middle x
for i in range(target[0] // 2):
    master_route_board[x][y] = [count, equipped]
    next_sq = board[x + 1][y]
    if next_sq == ".":
        if equipped == NOTHING:
            equipped = TORCH
            count += 7
    elif next_sq == "=":
        if equipped == TORCH:
            equipped = GEAR
            count += 7
    elif next_sq == "|":
        if equipped == GEAR:
            equipped = TORCH
            count += 7
    else:
        raise Exception("FFS!")

    x += 1
    count += 1

# Move down until level with target
for i in range(target[1]):
    master_route_board[x][y] = [count, equipped]
    next_sq = board[x][y + 1]
    if next_sq == ".":
        if equipped == NOTHING:
            equipped = TORCH
            count += 7
    elif next_sq == "=":
        if equipped == TORCH:
            equipped = GEAR
            count += 7
    elif next_sq == "|":
        if equipped == GEAR:
            equipped = TORCH
            count += 7
    else:
        raise Exception("FFS!")

    y += 1
    count += 1

# Move right to target
for i in range(target[0]):
    if x < target[0]:
        master_route_board[x][y] = [count, equipped]
        next_sq = board[x + 1][y]
        if next_sq == ".":
            if equipped == NOTHING:
                equipped = TORCH
                count += 7
        elif next_sq == "=":
            if equipped == TORCH:
                equipped = GEAR
                count += 7
        elif next_sq == "|":
            if equipped == GEAR:
                equipped = TORCH
                count += 7
        else:
            raise Exception("FFS!")

        x += 1
        count += 1

# Switch to torch
if (x, y) == target:
    if equipped != TORCH:
        count += 7
    master_route_board[x][y] = [count, equipped]


best_case = master_route_board[x][y][0]


def print_route(route_board):
    for y in range(height):
        line = ""
        for x in range(width):
            if (x, y) == target:
                line += " {}  ".format("T")
            elif route_board[x][y][0] is None:
                line += " {}  ".format("#")
            elif route_board[x][y][0] < 10:
                line += " {}  ".format(route_board[x][y][0])
            else:
                line += " {} ".format(route_board[x][y][0])
        print(line)


print_route(master_route_board)

# Try a random walk
import random


def pick_tool(choices):
    i = random.randint(0, len(choices) - 1)
    return choices[i]


# master_route_board = [[[None, None] for y in range(height)] for x in range(width)]

for _ in range(100):
    x = 0
    y = 0
    count = 0
    equipped = TORCH

    route_board = [[[None, None] for y in range(height)] for x in range(width)]

    try:
        while (x, y) != target:
            route_board[x][y] = [count, equipped]
            if (
                master_route_board[x][y][0] is None
                or master_route_board[x][y][0] > count
            ):
                master_route_board[x][y] = [count, equipped]
            elif master_route_board[x][y][0] < count:
                count = master_route_board[x][y][0]
                equipped = master_route_board[x][y][1]

            # Get options
            options = []
            if x > 0 and route_board[x - 1][y][0] is None:
                # Biase towards target
                if x > target[0]:
                    options.append((x - 1, y))
                # Biase to terrain
                # if board[x - 1][y] == "." and equipped in [TORCH, GEAR]:
                #     options.append((x - 1, y))
                # elif board[x - 1][y] == "=" and equipped in [NOTHING, GEAR]:
                #     options.append((x - 1, y))
                # elif board[x - 1][y] == "|" and equipped in [NOTHING, TORCH]:
                #     options.append((x - 1, y))
                options.append((x - 1, y))
            if y > 0 and route_board[x][y - 1][0] is None:
                if x == 0:
                    # Don't go up
                    pass
                else:
                    if y > target[1]:
                        options.append((x, y - 1))
                    # if board[x][y - 1] == "." and equipped in [TORCH, GEAR]:
                    #     options.append((x, y - 1))
                    # elif board[x][y - 1] == "=" and equipped in [NOTHING, GEAR]:
                    #     options.append((x, y - 1))
                    # elif board[x][y - 1] == "|" and equipped in [NOTHING, TORCH]:
                    #     options.append((x, y - 1))
                    options.append((x, y - 1))
            if route_board[x + 1][y][0] is None:
                if x < target[0]:
                    options.append((x + 1, y))
                # if board[x + 1][y] == "." and equipped in [TORCH, GEAR]:
                #     options.append((x + 1, y))
                # elif board[x + 1][y] == "=" and equipped in [NOTHING, GEAR]:
                #     options.append((x + 1, y))
                # elif board[x + 1][y] == "|" and equipped in [NOTHING, TORCH]:
                #     options.append((x + 1, y))
                options.append((x + 1, y))
            if route_board[x][y + 1][0] is None:
                if y < target[1]:
                    options.append((x, y + 1))
                    options.append((x, y + 1))
                    options.append((x, y + 1))
                # if board[x][y + 1] == "." and equipped in [TORCH, GEAR]:
                #     options.append((x, y + 1))
                # elif board[x][y + 1] == "=" and equipped in [NOTHING, GEAR]:
                #     options.append((x, y + 1))
                # elif board[x][y + 1] == "|" and equipped in [NOTHING, TORCH]:
                #     options.append((x, y + 1))
                options.append((x, y + 1))
            if len(options) == 0:
                # Hit dead end
                # print_route(route_board)
                raise Exception("Deadend")
            i = random.randint(0, len(options) - 1)

            x, y = options[i]
            next_sq = board[x][y]
            if next_sq == ".":
                if equipped == NOTHING:
                    equipped = pick_tool([TORCH, GEAR])
                    count += 7
            elif next_sq == "=":
                if equipped == TORCH:
                    equipped = pick_tool([NOTHING, GEAR])
                    count += 7
            elif next_sq == "|":
                if equipped == GEAR:
                    equipped = pick_tool([NOTHING, TORCH])
                    count += 7
            else:
                raise Exception("FFS!")

            count += 1

            if count > best_case:
                raise Exception("Getting worse")
    except Exception as err:
        # print(err)
        continue

    if (x, y) == target:
        if equipped != TORCH:
            count += 7
            route_board[x][y][0] = count

    if count < best_case:
        print_route(route_board)
        best_case = count
        print("Best is", best_case)

print_route(master_route_board)
