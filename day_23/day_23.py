import re

with open("input.txt") as f:
    PUZZLE_INPUT = f.read().strip()

# PUZZLE_INPUT = """
# pos=<10,12,12>, r=2
# pos=<12,14,12>, r=2
# pos=<16,12,12>, r=4
# pos=<14,14,14>, r=6
# pos=<50,50,50>, r=200
# pos=<10,10,10>, r=5
# """


bots = set()
max_range = 0
max_bot = None

for line in PUZZLE_INPUT.splitlines():
    if m := re.match(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)", line):
        bot = (
            int(m.groups()[0]),
            int(m.groups()[1]),
            int(m.groups()[2]),
            int(m.groups()[3]),
        )
        bots.add(bot)
        if bot[3] > max_range:
            max_bot = bot
            max_range = bot[3]

num_in = 0

for b in bots:
    if b == max_bot:
        num_in += 1
        continue
    diff = abs(b[0] - max_bot[0]) + abs(b[1] - max_bot[1]) + abs(b[2] - max_bot[2])
    if diff <= max_range:
        num_in += 1
print(max_bot)

# 599
print(f"Part 1: {num_in}")


# Part 2
# Find starting bounds
min_x = float("inf")
min_y = float("inf")
min_z = float("inf")
max_x = float("-inf")
max_y = float("-inf")
max_z = float("-inf")

for b in bots:
    min_x = min(b[0], min_x)
    min_y = min(b[1], min_y)
    min_z = min(b[2], min_z)
    max_x = max(b[0], max_x)
    max_y = max(b[1], max_y)
    max_z = max(b[2], max_z)

mins = [min_x, min_y, min_z]
maxs = [max_x, max_y, max_z]

grid_size = maxs[0] - mins[0]

best_grid = None

while grid_size > 0:
    max_count = -1

    for x in range(mins[0], maxs[0] + 1, grid_size):
        for y in range(mins[1], maxs[1] + 1, grid_size):
            for z in range(mins[2], maxs[2] + 1, grid_size):
                # See how many bots are in the grid centered on the "origin"
                count = 0
                for bx, by, bz, br in bots:
                    # Calculate the distance from the origin of the grid
                    dist = abs(bx - x) + abs(by - y) + abs((bz - z))
                    # Check if the bot's signal is within range
                    if dist - br < grid_size:
                        count += 1

                if count > max_count:
                    # Grid contains more bots
                    max_count = count
                    best_grid = [x, y, z]
                elif count == max_count and (abs(x) + abs(y) + abs(z)) < (
                    abs(best_grid[0]) + abs(best_grid[1]) + abs(best_grid[2])
                ):
                    # Update only if nearer to origin than previous solution
                    best_grid = [x, y, z]

    print(grid_size, max_count, best_grid)

    # For the next turn work on the region around the best solution
    mins[0] = best_grid[0] - grid_size
    mins[1] = best_grid[1] - grid_size
    mins[2] = best_grid[2] - grid_size
    maxs[0] = best_grid[0] + grid_size
    maxs[1] = best_grid[1] + grid_size
    maxs[2] = best_grid[2] + grid_size

    grid_size //= 2

# 94481130
print(f"Part 2: {sum(best_grid)}")
