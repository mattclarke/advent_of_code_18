import re


with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


class Star:
    def __init__(self, pos, velocity):
        self.pos = pos
        self.velocity = velocity

    def update(self):
        self.pos = (self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1])


data = []

for d in PUZZLE_INPUT.splitlines():
    m = re.match(r".+<\s*([-\d]+),\s*([-\d]+)> velocity=<\s*([-\d]+),\s*([-\d]+)>", d)
    if not m:
        print("Ooops", d)
        raise Exception("re fail!")
    data.append(
        Star(
            (int(m.groups()[0]), int(m.groups()[1])),
            (int(m.groups()[2]), int(m.groups()[3])),
        )
    )


def print_layout(positions):
    min_x = float("inf")
    max_x = float("-inf")
    min_y = float("inf")
    max_y = float("-inf")

    for p in positions:
        min_x = min(p[0], min_x)
        max_x = max(p[0], max_x)
        min_y = min(p[1], min_y)
        max_y = max(p[1], max_y)

    for j in range(min_y - 1, max_y + 2):
        line = ""
        for i in range(min_x - 1, max_x + 2):
            if (i, j) in positions:
                line += "#"
            else:
                line += "."
        print(line)


spread_x = None
spread_y = None
minned = False
positions = []
seconds = 0

while True:
    old_positions = positions[:]
    positions = []

    min_x = float("inf")
    max_x = float("-inf")
    min_y = float("inf")
    max_y = float("-inf")

    for d in data:
        d.update()
        min_x = min(d.pos[0], min_x)
        max_x = max(d.pos[0], max_x)
        min_y = min(d.pos[1], min_y)
        max_y = max(d.pos[1], max_y)
        positions.append((d.pos[0], d.pos[1]))

    x_minned = False
    y_minned = False

    if spread_x is None:
        spread_x = max_x - min_x
        spread_y = max_y - min_y
    else:
        if max_x - min_x <= spread_x:
            spread_x = max_x - min_x
            x_minned = True
        if max_y - min_y <= spread_y:
            spread_y = max_y - min_y
            y_minned = True

    if x_minned and y_minned:
        minned = True
    else:
        if minned:
            # Starting to disperse
            print("Dispersing")
            # Eyeball the answer to Part 1: GFNKCGGH
            print_layout(old_positions)
            break
    seconds += 1


# 10274
print(f"Part 2: {seconds}")
