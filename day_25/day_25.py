import re

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

input_data = PUZZLE_INPUT
points = []

for line in input_data.splitlines():
    if not line:
        continue
    m = re.match(r"\s?(-?\d+),(-?\d+),(-?\d+),(-?\d+)", line)
    if m:
        # print(m.groups())
        raw = m.groups()
        points.append((int(raw[0]), int(raw[1]), int(raw[2]), int(raw[3])))
    else:
        raise Exception("WTF!", line)


def calc_distance(p1, p2):
    dist = 0
    for i in range(4):
        dist += abs(p1[i] - p2[i])
    return dist


class Cloud:
    def __init__(self):
        self.points = []

    def can_add(self, point):
        if len(self.points) == 0:
            return True

        for p in self.points:
            dist = calc_distance(point, p)
            if dist <= 3:
                return True

        return False

    def can_merge(self, cloud):
        for p in self.points:
            if cloud.can_add(p):
                return True

        return False


clouds = [Cloud()]

for p in points:
    added = False
    for c in clouds:
        if c.can_add(p):
            c.points.append(p)
            added = True
            break

    # Could not add to existing cloud
    if not added:
        clouds.append(Cloud())
        clouds[-1].points.append(p)

# Now we have some small clouds, now to see if they can merge
changes = 1

while changes != 0:
    changes = 0
    new_clouds = []
    i = 0
    while i < len(clouds):
        if len(clouds[i].points) == 0:
            i += 1
            continue
        j = i + 1
        while j < len(clouds):
            if len(clouds[j].points) == 0:
                j += 1
                continue
            if clouds[i].can_merge(clouds[j]):
                clouds[i].points.extend(clouds[j].points)
                clouds[j].points = []
                changes += 1
            j += 1
        i += 1

    for c in clouds:
        if len(c.points) > 0:
            new_clouds.append(c)

    clouds = new_clouds[:]

# 388
print("Part 1:", len(clouds))
