import re

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

bots = set()
max_range = 0
max_bot = None

for line in PUZZLE_INPUT.splitlines():
    if not line:
        continue
    m = re.match(r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)", line)
    if m:
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
    else:
        raise Exception("WTF!")

num_in = 0

for b in bots:
    if b == max_bot:
        num_in += 1
        continue
    diff = abs(b[0] - max_bot[0]) + abs(b[1] - max_bot[1]) + abs(b[2] - max_bot[2])
    if diff <= max_range:
        num_in += 1

# 599
print(f"Part 1: {num_in}")
