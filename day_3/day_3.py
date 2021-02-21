with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


# Part 1
def parse_input(input):
    input = (
        input.replace("#", "")
        .replace("@", "")
        .replace(":", "")
        .replace("x", " ")
        .replace(",", " ")
    )
    parts = input.split()
    return {
        "n": int(parts[0]),
        "x": int(parts[1]),
        "y": int(parts[2]),
        "w": int(parts[3]),
        "h": int(parts[4]),
    }


def print_grid(grid, x, y):
    for j in range(y + 2):
        row = ""
        for i in range(x + 2):
            key = "{},{}".format(i, j)
            if key in grid:
                row += str(grid[key])
            else:
                row += "."
        print(row)


grid = {}
ans = 0
max_x = 0   # For plotting only
max_y = 0   # For plotting only

for d in PUZZLE_INPUT.splitlines():
    info = parse_input(d)

    for i in range(info["w"]):
        for j in range(info["h"]):
            pos_x = info["x"] + i
            pos_y = info["y"] + j
            max_x = max(max_x, pos_x)
            max_y = max(max_y, pos_y)
            key = "{},{}".format(pos_x, pos_y)
            if key in grid:
                if grid[key] != "X":
                    ans += 1
                grid[key] = "X"
            else:
                grid[key] = info["n"]

# 111266
print(f"Part 1: {ans}")

# Part 2
for d in PUZZLE_INPUT.splitlines():
    info = parse_input(d)
    overlapped = False

    for i in range(info["w"]):
        for j in range(info["h"]):
            pos_x = info["x"] + i
            pos_y = info["y"] + j
            key = "{},{}".format(pos_x, pos_y)
            if grid[key] == "X":
                overlapped = True
                break
        if overlapped:
            break
    if not overlapped:
        # 266
        print(f"Part 2: {info['n']}")
