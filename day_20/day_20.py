import re

with open("input.txt") as f:
    PUZZLE_INPUT = f.read().strip()


def solve(input_str):
    input_str = input_str.replace("^","").replace("$","")
    # Reduce
    while match := re.search(r"\([A-Z]+\|[A-Z\|]*\)", input_str):
        start = match.span()[0]
        end = match.span()[1]
        temp = input_str[start:end].replace("(", "").replace(")", "")
        parts = temp.split("|")
        longest = parts[0]
        for p in parts:
            if p == "":
                longest = ""
                break
            if len(p) > len(longest):
                longest = p
        prefix = input_str[0:start]
        suffix = input_str[end:]
        input_str = prefix + longest + suffix
    return input_str


EXAMPLE_1 = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"
assert len(solve(EXAMPLE_1)) == 31

EXAMPLE_2 = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
assert len(solve(EXAMPLE_2)) == 23

EXAMPLE_3 = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
assert len(solve(EXAMPLE_3)) == 18

result = solve(PUZZLE_INPUT)
# 3788 - I think this is a fluke though...
print(f"Part 1: {len(result)}")

directions = {
    "N": lambda coords: (coords[0], coords[1] + 1),
    "E": lambda coords: (coords[0] + 1, coords[1]),
    "S": lambda coords: (coords[0], coords[1] - 1),
    "W": lambda coords: (coords[0] - 1, coords[1]),
}


def solve(puzzle):
    locations = {
        (0, 0): 0
    }

    index = 1
    position = (0, 0)
    distance = 0
    stack = []

    # ( is a push
    # | is a peek
    # ) is a pop
    # |) means we are back to the position before the (

    while puzzle[index] != "$":
        if puzzle[index].isalpha():
            position = directions[puzzle[index]](position)
            distance += 1
            stored = locations.get(position, distance)
            locations[position] = min(stored, distance)
            index += 1
        elif puzzle[index] == "(":
            stack.append((position, distance))
            index += 1
        elif puzzle[index] == "|":
            position, distance = stack[~0]
            index += 1
        elif puzzle[index] == ")":
            position, distance = stack.pop()
            index += 1

    max_dist = 0
    count = 0
    for v in locations.values():
        if v >= 1000:
            count +=1

        if v > max_dist:
            max_dist = v
    return max_dist, count


assert solve(EXAMPLE_1)[0] == 31
assert solve(EXAMPLE_2)[0] == 23
assert solve(EXAMPLE_3)[0] == 18
part_1, part_2 = solve((PUZZLE_INPUT))

# 3788
print(f"Part 1: {part_1}")

# 8568
print(f"Part 2: {part_2}")
