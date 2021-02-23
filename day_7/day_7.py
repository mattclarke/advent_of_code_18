with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


# Part 1
import re


def extract_letters(data):
    m = re.match(r"Step ([A-Z]) must be finished before step ([A-Z])", data)
    return m.groups()[0], m.groups()[1]


class Node:
    def __init__(self, letter):
        self.letter = letter
        self.done = False
        self.before = []
        self.after = []
        self.time_required = 0  # Used in part 2
        self.in_progress = False  # Used in part 2


# Construct graph
def construct_graph():
    nodes = {}
    for d in PUZZLE_INPUT.splitlines():
        i, j = extract_letters(d)
        if i not in nodes:
            nodes[i] = Node(i)
            nodes[i].after.append(j)
        else:
            nodes[i].after.append(j)

        if j not in nodes:
            nodes[j] = Node(j)
            nodes[j].before.append(i)
        else:
            nodes[j].before.append(i)
    return nodes


nodes = construct_graph()


def parents_done(n):
    for p in n.before:
        if not nodes[p].done:
            return False
    return True


# Find start
start = None

for k, v in nodes.items():
    if len(v.before) == 0:
        # print("Start at {}".format(k))
        start = k
        v.done = True
        break

ans = [start]


def get_options(all_nodes):
    options = []
    for k, v in all_nodes.items():
        if not v.done and parents_done(v) and not v.in_progress:
            options.append(k)
    return options


while True:
    opts = get_options(nodes)
    if len(opts) == 0:
        break

    # Sort
    opts.sort()
    # print("{} from {}".format(opts[0], opts))
    nodes[opts[0]].done = True
    ans.append(opts[0])

# IJLFUVDACEHGRZPNKQWSBTMXOY
print(f"Part 1: {''.join(ans)}")

# Part 2
alpha = [chr(i) for i in range(65, 91)]
step_time = 60  # 0 for example data
num_workers = 5  # 2 for example data
nodes = construct_graph()

# Update the required_times
for k, v in nodes.items():
    v.time_required = step_time + alpha.index(k) + 1

ans = []
total_time = 0
workers = ["." for i in range(num_workers)]


while len(ans) < len(nodes):
    opts = get_options(nodes)
    worker_freed = False

    # Sort
    opts.sort()

    # Assign work
    for i, w in enumerate(workers):
        if w == ".":
            if len(opts) > 0:
                n = opts.pop(0)
                workers[i] = n
                nodes[n].in_progress = True
        else:
            if nodes[w].time_required == 0:
                ans.append(w)
                nodes[w].done = True
                workers[i] = "."
                worker_freed = True

    # Move forward in time
    if not worker_freed:
        for w in workers:
            if w != ".":
                nodes[w].time_required -= 1

        # print("{} {} {}".format(total_time, " ".join(workers), "".join(ans)))
        total_time += 1

# 1072
print(f"Part 2: {total_time}")
