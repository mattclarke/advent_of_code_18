with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


class Node:
    def __init__(self, nc, nm, parent, num):
        self.name = str(num)
        self.num_children = nc
        self.num_meta = nm
        self.children = []
        self.metadata = []
        self.parent = parent
        self.total = 0


# Part 1
data = [int(x) for x in PUZZLE_INPUT.split()]

nodes = []
num = 0


def process(n, i, num):
    if i >= len(data):
        raise Exception("Done!")

    curr = Node(data[i], data[i + 1], n, num)
    if n is not None:
        n.children.append(curr)

    i += 2
    for c in range(curr.num_children):
        i = process(curr, i, num + 1)

    for m in range(curr.num_meta):
        curr.metadata.append(data[i])
        curr.total += data[i]
        i += 1

    nodes.append(curr)
    return i


try:
    process(None, 0, 0)
except:
    pass

total = 0
for n in nodes:
    total += n.total

# 41555
print(f"Part 1: {total}")

# Part 2
root_node = nodes[-1]


def process2(n):
    value = 0

    if len(n.children) == 0:
        return n.total

    for i in n.metadata:
        j = i - 1
        if j < len(n.children):
            value += process2(n.children[j])

    return value


# 16653
print(f"Part 2: {process2(root_node)}")
