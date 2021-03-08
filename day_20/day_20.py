import re

with open("input.txt") as f:
    PUZZLE_INPUT = f.read().strip()

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

result = solve(PUZZLE_INPUT)
# 3788 - I think this is a fluke
print(f"Part 1: {len(result)}")

directions = {
    "N": (0, 1),
    "E": (1, 0),
    "S": (0, -1),
    "W": (-1, 0),
}


class Node:
    def __init__(self, string):
        self.string = string
        self.children = []
        self.parents = []

    def __repr__(self):
        return self.string


def build_graph(input_str):
    def _is_dir(previous, index):
        node = Node(input_str[index])
        for p in previous:
            p.children.append(node)
            node.parents.append(p)
        return [node], index + 1

    def _is_open(previous, index):
        temp = previous
        loose_ends = []
        while index < len(input_str):
            if input_str[index].isalpha():
                temp, index = _is_dir(temp, index)
            elif input_str[index] == "|":
                loose_ends.extend(temp)
                temp = previous
                index += 1
                if input_str[index] == ")":
                    # |)
                    loose_ends.extend(previous)
                    return loose_ends, index + 1
            elif input_str[index] == ")":
                loose_ends.extend(temp)
                return loose_ends, index + 1
            elif input_str[index] == "(":
                temp, index = _is_open(temp, index + 1)

    def _build(previous, index=1):
        temp = previous

        while index < len(input_str):
            if input_str[index].isalpha():
                node, index = _is_dir(temp, index)
                temp = node
            elif input_str[index] == "(":
                temp, index = _is_open(temp, index + 1)
            elif input_str[index] == "$":
                index += 1
                node = Node("$")
                for t in temp:
                    t.children.append(node)
                    node.parents.append(t)
            else:
                assert False, "unexpected"

    head = Node("^")
    _build([head])
    return head


# build_graph("^NESW$")
# build_graph("^NE(A|B|C)$")
# build_graph("^NE(A|B(C|D))$")
# build_graph("^NE(A|B(C|D|E)F)$")
# build_graph("^N(A|B(C|D(E|F)))$")
# build_graph("^W(S|N(E(A|B)|C(D|F(G|H))))$")
# build_graph("^N(A|B|)F$")

graph = build_graph(PUZZLE_INPUT)
# print(graph)

queue = [(graph,0)]
scores = {

}

while queue:
    node, depth = queue.pop(0)
    if node not in scores:
        scores[node] = (depth, depth)
    else:
        if depth > scores[node][0] or depth < scores[node][1]:
            long = max(depth, scores[node][0])
            short = min(depth, scores[node][1])
            scores[node] = (long, short)
        else:
            continue
    first = True
    for child in node.children:
        if first:
            queue.insert(0, (child, depth + 1))
            first = False
            continue
        queue.append((child, depth + 1))


furthest = scores[graph]
node = graph

for k, v in scores.items():
    if str(k) == "$":
        continue
    if v[0] > furthest[0]:
        furthest = v
        node = k

print(furthest)

target = node
route = [str(target)]

while str(node) != "^":
    best_p = node.parents[0]
    dist = scores[best_p][1]
    for p in node.parents:
        if p == best_p:
            continue
        if scores[p][1] < dist:
            best_p = p
            dist = scores[p][1]
        elif scores[p][1] == dist:
            print("two")
    node = best_p
    route.insert(0, str(node))

print(result, len(result))
print("".join(route[1:]))

count = 0
for k,v in scores.items():
    if str(k) == "$":
        continue

    if v[1] > 1000:
        count += 1

# 9557 is too high
print(count)
