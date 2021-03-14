with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


test_data = """
.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.
"""

raw_data = PUZZLE_INPUT
size = len(raw_data.splitlines()[1])
print(size)

board = [[" " for y in range(size)] for x in range(size)]

y = 0
for line in raw_data.splitlines():
    if not line:
        continue
    for x, c in enumerate(line):
        board[x][y] = c
    y += 1


def print_board(board):
    for y in range(len(board[0])):
        line = ""
        for x in range(len(board)):
            line += board[x][y]
        print(line)
    print()


def board_to_string(board):
    lines = []
    for y in range(len(board[0])):
        line = ""
        for x in range(len(board)):
            line += board[x][y]
        lines.append(line)
    return "".join(lines)


def get_adjacent(board, x, y):
    adjacent = []
    if x == 0 and y == 0:
        # Top left
        adjacent.append(board[x + 1][y])
        adjacent.append(board[x + 1][y + 1])
        adjacent.append(board[x][y + 1])
    elif x == 0 and y == len(board[0]) - 1:
        # Bottom left
        adjacent.append(board[x + 1][y])
        adjacent.append(board[x + 1][y - 1])
        adjacent.append(board[x][y - 1])
    elif x == 0:
        # Left side
        adjacent.append(board[x][y - 1])
        adjacent.append(board[x + 1][y - 1])
        adjacent.append(board[x + 1][y])
        adjacent.append(board[x + 1][y + 1])
        adjacent.append(board[x][y + 1])
    elif x == len(board) - 1 and y == 0:
        # Top right
        adjacent.append(board[x - 1][y])
        adjacent.append(board[x - 1][y + 1])
        adjacent.append(board[x][y + 1])
    elif x == len(board) - 1 and y == len(board[0]) - 1:
        # Bottom right
        adjacent.append(board[x - 1][y])
        adjacent.append(board[x - 1][y - 1])
        adjacent.append(board[x][y - 1])
    elif x == len(board) - 1:
        # Left side
        adjacent.append(board[x][y - 1])
        adjacent.append(board[x - 1][y - 1])
        adjacent.append(board[x - 1][y])
        adjacent.append(board[x - 1][y + 1])
        adjacent.append(board[x][y + 1])
    elif y == 0:
        # Top row
        adjacent.append(board[x - 1][y])
        adjacent.append(board[x - 1][y + 1])
        adjacent.append(board[x][y + 1])
        adjacent.append(board[x + 1][y + 1])
        adjacent.append(board[x + 1][y])
    elif y == len(board[0]) - 1:
        # Bottom row
        adjacent.append(board[x - 1][y])
        adjacent.append(board[x - 1][y - 1])
        adjacent.append(board[x][y - 1])
        adjacent.append(board[x + 1][y - 1])
        adjacent.append(board[x + 1][y])
    else:
        # Everywhere else
        adjacent.append(board[x - 1][y])
        adjacent.append(board[x - 1][y - 1])
        adjacent.append(board[x][y - 1])
        adjacent.append(board[x + 1][y - 1])
        adjacent.append(board[x + 1][y])
        adjacent.append(board[x + 1][y + 1])
        adjacent.append(board[x][y + 1])
        adjacent.append(board[x - 1][y + 1])

    return adjacent


def evolve(board, x, y):
    temp = board[x][y]
    adjacent = get_adjacent(board, x, y)
    if board[x][y] == ".":
        if adjacent.count("|") >= 3:
            return "|"
        else:
            return "."
    elif board[x][y] == "|":
        if adjacent.count("#") >= 3:
            return "#"
        else:
            return "|"
    elif board[x][y] == "#":
        if adjacent.count("#") > 0 and adjacent.count("|") > 0:
            return "#"
        else:
            return "."

    raise Exception("Oops")


print_board(board)
count_trees = 0
count_yards = 0
values = set()
reps = []
prev_reps = []
rep_count = 0

patterns = {

}

found_repeat = False
repeat_distance = 0

i = 0

while i < 1_000_000_000:
    i += 1
    count_trees = 0
    count_yards = 0
    next_board = [[" " for y in range(size)] for x in range(size)]
    print(f"After {i} minutes:")
    for y in range(len(board[0])):
        for x in range(len(board)):
            next_board[x][y] = evolve(board, x, y)
            if next_board[x][y] == "|":
                count_trees += 1
            elif next_board[x][y] == "#":
                count_yards += 1

    board = next_board
    if not found_repeat:
        as_str = board_to_string(board)
        if as_str in patterns:
            print(f"Pattern match {i} {patterns[as_str]}")
            repeat_distance = i - patterns[as_str]
            found_repeat = True
            multiplier = 1000000
            while multiplier > 1:
                if i < 1_000_000_000 - repeat_distance * multiplier:
                    i += repeat_distance * multiplier
                else:
                    multiplier //= 10
                print(i)
        else:
            patterns[as_str] = i
    # print_board(board)
    # print(count_trees, count_yards, count_trees * count_yards)

    # Comment this out for part 1 and change range to 10
    # if count_trees * count_yards not in values:
    #     reps = [count_trees * count_yards]
    #     values.add(count_trees * count_yards)
    #     print("Restarting")
    # else:
    #     if count_trees * count_yards in reps:
    #         if not prev_reps:
    #             prev_reps = reps[:]
    #         elif prev_reps == reps:
    #             rep_count += 1
    #             # Wait for 10 consecutive matches to be safe
    #             if rep_count == 10:
    #                 temp = 1000000000 - (i + 1)
    #                 rem = temp % len(reps)
    #                 print(reps[rem])
    #                 break
    #         else:
    #             prev_reps = reps[:]
    #             rep_count = 0
    #         print("match", len(reps), reps[0], reps[-1])
    #
    #         reps = [count_trees * count_yards]
    #     else:
    #         reps.append(count_trees * count_yards)

# Part 1 = 621205
# Part 2 = 228490
print(count_trees * count_yards)
