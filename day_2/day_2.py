with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

# Part 1
twos = 0
threes = 0

for id in PUZZLE_INPUT.splitlines():
    counts = {}
    twice = 0
    thrice = 0

    for c in id:
        if c not in counts:
            counts[c] = 1
        elif counts[c] == 1:
            counts[c] += 1
            twice += 1
        elif counts[c] == 2:
            counts[c] += 1
            twice -= 1
            thrice += 1

    if twice > 0:
        twos += 1
    if thrice > 0:
        threes += 1

# 5952
print("Part 1: {}".format(twos * threes))


# Part 2
def compare_ids(a, b):
    mismatches = 0
    matched_str = ""

    for i, j in zip(a, b):
        if i != j:
            mismatches += 1
        else:
            matched_str += i
    return mismatches, matched_str


ids = PUZZLE_INPUT.splitlines()
result = None

for i, v1 in enumerate(ids):
    for v2 in ids[i + 1 :]:
        ans = compare_ids(v1, v2)
        if ans[0] == 1:
            result = ans[1]

# krdmtuqjgwfoevnaboxglzjph
print("Part 2:", result)
