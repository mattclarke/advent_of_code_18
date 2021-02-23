def find_power(x, y, gsn):
    rack_id = x + 10
    power = rack_id * y
    power += gsn
    power *= rack_id
    if power < 100:
        return 0
    power //= 100
    power %= 10
    return power - 5


assert 4 == find_power(3, 5, 8)
assert -5 == find_power(122, 79, 57)
assert 0 == find_power(217, 196, 39)
assert 4 == find_power(101, 153, 71)

# Part 1
PUZZLE_INPUT = 8141  # grid serial number
x_range = 300
y_range = 300

energies = []

for x in range(x_range):
    col = []
    for y in range(y_range):
        e = find_power(x, y, PUZZLE_INPUT)
        col.append(e)
    energies.append(col)


def calc_area_power(x, y, en, s):
    total = 0
    for i in range(s):
        for j in range(s):
            total += en[x + i][y + j]
    return total


p_max = 0
x_max = 0
y_max = 0

for i in range(x_range - 2):
    for j in range(y_range - 2):
        p = calc_area_power(i, j, energies, 3)
        if p > p_max:
            p_max = p
            x_max = i
            y_max = j

# 235, 16
print(f"Part 1: {x_max}, {y_max}")

# Part 2
p_max = float("-inf")
x_max = 0
y_max = 0
size = 0
cache = {}


def calc_area_power_cached(x, y, en, s):
    key = "{} {}".format(x, y)
    if key in cache:
        # Add new "lines" only
        total = cache[key]

        for i in range(s):
            # print(en[x + s][y + i])
            total += en[x + s][y + i]
            # print(en[x + i][y + s])
            total += en[x + i][y + s]

        # And the corner
        total += en[x + s][y + s]
    else:
        total = en[x][y]
    cache[key] = total
    return total


for s in range(x_range):
    # print(s)
    for i in range(x_range):
        for j in range(x_range):
            if i + s < x_range and j + s < y_range:
                # print(s, i,j)
                p = calc_area_power_cached(i, j, energies, s)
                if p > p_max:
                    p_max = p
                    x_max = i
                    y_max = j
                    size = s + 1

# 236, 227, 14
print(f"Part 2: {x_max}, {y_max}, {size}")
