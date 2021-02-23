import collections

initial = ".#..##..#.....######.....#....####.##.#.#...#...##.#...###..####.##.##.####..######......#..##.##.##"

raw_rules = """#.... => .
.##.# => #
#..## => .
....# => .
###.# => #
...#. => #
#...# => #
#.### => .
.#... => #
...## => .
..### => .
####. => .
##.## => .
..##. => .
.#.## => #
#..#. => #
..... => .
#.#.. => .
##.#. => #
.#### => #
##### => .
#.##. => #
.#..# => #
##... => .
..#.# => #
##..# => #
.###. => .
.#.#. => #
#.#.# => #
###.. => .
.##.. => .
..#.. => .
"""


# Extract rules
def extract_rule(rule):
    import re

    m = re.match(r"([#.]{5}) => ([#.])", r)
    if not m:
        print("oops")
        raise Exception("Rule exception")

    if m.groups()[1] == "#":
        return m.groups()[0], True
    else:
        return m.groups()[0], False


rules = {}

for r in raw_rules.splitlines():
    k, v = extract_rule(r)
    rules[k] = v


def solve(part_2=False):
    # Extract initial state

    state = collections.deque()
    zeroth = 0
    old_zeroth = 0

    for i in initial:
        state.append(i)

    # print("".join(state))

    # Part 1 and 2
    prev_states = None
    same_z = 0

    generations = 50_000_000_000 if part_2 else 20

    for z in range(generations):
        old_zeroth = zeroth

        # Tidy up by removing leading "."
        while True:
            if state[0] == "#":
                break
            state.popleft()
            zeroth -= 1

        for i in range(4):
            state.appendleft(".")
            zeroth += 1

        # if z % 1000 == 0:
        #     print("".join(state))

        prev2 = "."
        prev1 = "."

        for i, s in enumerate(state):
            # Pad end
            if i == len(state) - 2:
                key = "{}{}{}{}{}".format(prev2, prev1, s, state[i + 1], ".")
            elif i == len(state) - 1:
                key = "{}{}{}{}{}".format(prev2, prev1, s, ".", ".")
            else:
                key = "{}{}{}{}{}".format(prev2, prev1, s, state[i + 1], state[i + 2])
            # print(key)

            prev2 = prev1
            prev1 = s

            if key in rules:
                if rules[key]:
                    state[i] = "#"
                else:
                    state[i] = "."
            else:
                state[i] = "."

        # Check states after "end"
        e1 = prev2 + prev1 + "..."
        e2 = prev1 + "...."

        add_e1 = False
        add_e2 = False

        if e2 in rules and rules[e2]:
            add_e2 = True
            add_e1 = True
        elif e1 in rules and rules[e1]:
            add_e1 = True

        if add_e1:
            state.append("#" if rules[e1] else ".")
        if add_e2:
            state.append("#" if rules[e2] else ".")

        # print("".join(state))
        if prev_states == state:
            # At some point the answer stops changing except the zeroth moves
            # So bulk adjust zeroth and exit
            if zeroth < old_zeroth:
                zeroth -= 50000000000 - 1 - z
            else:
                zeroth += 50000000000 - 1 - z
            break

        prev_states = state.copy()

    # Calculate total
    total = 0
    for i, s in enumerate(state):
        if s == "#":
            total += i - zeroth
    return total


# Part 1
total = solve()

# 3605
print(f"Part 1: {total}")

# Part 2
total = solve(True)

# 4050000000798
print(f"Part 2: {total}")
