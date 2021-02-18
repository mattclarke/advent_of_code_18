with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# Part 1
total = 0

for i in PUZZLE_INPUT.splitlines():
    total += int(i)

# 437
print(f"Part 1 = {total}")

# Part 2
total = 0
values = {0}
result = 0

found_duplicate = False

while not found_duplicate:
    for i in PUZZLE_INPUT.splitlines():
        total += int(i)
        if total in values:
            result = total
            found_duplicate = True
            break
        else:
            values.add(total)

# 655
print(f"Part 2 = {result}")
