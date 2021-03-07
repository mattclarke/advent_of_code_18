import re

with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

print(PUZZLE_INPUT)



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

# result = solve(PUZZLE_INPUT)
#
# print(f"Part 1: {len(result)}")
# print(result)
# print(len(result))
