with open("input.txt") as f:
    PUZZLE_INPUT = f.read()

EXAMPLE_1 = """
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
"""

EXAMPLE_2 = """
#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######
"""

EXAMPLE_3 = """
#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######
"""

EXAMPLE_4 = """
#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######
"""

EXAMPLE_5 = """
#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######
"""

EXAMPLE_6 = """
#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########
"""


def print_board(grid, elves, goblins, round, extras=None):
    print(f"After {round} rounds:")
    top = [str(x % 10) for x in range(len(grid[0]))]
    print(" " + "".join(top))

    y = len(grid)
    for y, row in enumerate(grid):
        line = [str(y % 10)]
        extra = []
        for x in range(len(row)):
            if (x, y) in elves:
                line.append("E")
                extra.append(f"E({elves[(x,y)]})")
            elif (x, y) in goblins:
                line.append("G")
                extra.append(f"G({goblins[(x, y)]})")
            elif extras and (x, y) in extras:
                line.append(str(extras[(x, y)] % 10))
            else:
                line.append(row[x])

        print("".join(line) + "   " + ",".join(extra))


def process_input(starting_grid):
    lines = starting_grid.strip().splitlines()
    y = 0
    grid = []
    goblins = {}
    elves = {}

    for y, line in enumerate(lines):
        row = []
        for x, c in enumerate(line):
            if c == "#" or c == ".":
                row.append(c)
            elif c == "E":
                row.append(".")
                elves[(x, y)] = 200
            elif c == "G":
                row.append(".")
                goblins[(x, y)] = 200
            else:
                assert False, "Something went badly wrong"
        grid.append(row)

    return grid, elves, goblins


def calculate_move_order(elves, goblins):
    order = []
    for e in elves:
        order.append((e, "E"))
    for g in goblins:
        order.append((g, "G"))

    order.sort(key=lambda x: x[0][0])
    order.sort(key=lambda x: x[0][1])
    return order


def find_closest_2(origin, grid, elves, goblins, possibles, debug=False):
    queue = [(origin, 0)]
    visited = {origin: 0}

    while queue:
        pos, distance = queue.pop(0)

        for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            npos = (pos[0] + x, pos[1] + y)

            if grid[npos[1]][npos[0]] == "#":
                continue
            if npos in elves or npos in goblins:
                continue

            if npos not in visited or distance + 1 < visited[npos]:
                visited[npos] = distance + 1
                queue.append((npos, distance + 1))

    if debug:
        print_board(grid, elves, goblins, "debug", visited)

    closest = []
    lowest = 10000000

    for poss in possibles:
        if poss not in visited:
            continue

        dist = visited[poss]
        if dist < lowest:
            closest = [poss]
            lowest = dist
        elif dist == lowest:
            closest.append(poss)

    solutions = []
    for close in closest:
        queue = [close]
        seen = set()

        while queue:
            pos = queue.pop(0)
            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                npos = (pos[0] + x, pos[1] + y)
                if npos == origin:
                    solutions.append(pos)
                    continue

                if npos in seen:
                    continue

                if npos in visited and visited[npos] < visited[pos]:
                    seen.add(npos)
                    queue.append(npos)
    return solutions


def find_closest(origin, grid, elves, goblins, possibles):
    queue = [[origin]]
    solutions = []
    lowest = 1000000000
    visited = {origin: 0}

    while queue:
        route = queue.pop(0)
        pos = route[~0]

        if len(route) > lowest:
            continue

        for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            npos = (pos[0] + x, pos[1] + y)
            # TODO: this doesn't work!
            if npos in visited and len(route) + 1 > visited[npos]:
                # Taken longer to get here so no point checking
                continue
            if grid[npos[1]][npos[0]] == "#":
                continue
            if npos in elves or npos in goblins:
                continue
            new_route = route + [npos]
            shortest = visited.get(npos, 10000000)
            visited[npos] = min(shortest, len(new_route))
            if npos in possibles:
                if len(new_route) > lowest:
                    continue

                if len(new_route) < lowest:
                    solutions.clear()
                # just need the first step
                solutions.append((new_route[1]))
                lowest = min(lowest, len(new_route))
                continue
            queue.append(new_route)
    return solutions


def get_adjacent(pos, enemy):
    result = []
    for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        npos = (pos[0] + x, pos[1] + y)
        if npos in enemy:
            result.append(npos)
    return result


def solve(starting_grid, elves_power=3):
    grid, elves, goblins = process_input(starting_grid)
    # print_board(grid, elves, goblins, 0)
    elves_killed = 0
    i = 0
    while True:
        round_finished = True
        order = calculate_move_order(elves, goblins)
        for pos, race in order:
            if race == "E" and pos in elves:
                adjacent = get_adjacent(pos, goblins)
                if not adjacent:
                    possible_spaces = gross_possibles(elves, goblins, grid, True)
                    possible_routes = find_closest_2(
                        pos, grid, elves, goblins, possible_spaces
                    )
                    possible_routes.sort(key=lambda x: x[0])
                    possible_routes.sort(key=lambda x: x[1])
                    if possible_routes:
                        choice = possible_routes[0]

                        hp = elves[pos]
                        del elves[pos]
                        elves[choice] = hp
                        adjacent = get_adjacent(choice, goblins)

                if adjacent:
                    do_attack(adjacent, goblins, elves_power)
            elif race == "G" and pos in goblins:
                adjacent = get_adjacent(pos, elves)
                if not adjacent:
                    possible_spaces = gross_possibles(elves, goblins, grid, False)
                    possible_routes = find_closest_2(
                        pos, grid, elves, goblins, possible_spaces
                    )
                    possible_routes.sort(key=lambda x: x[0])
                    possible_routes.sort(key=lambda x: x[1])
                    if possible_routes:
                        choice = possible_routes[0]

                        hp = goblins[pos]
                        del goblins[pos]
                        goblins[choice] = hp
                        adjacent = get_adjacent(choice, elves)

                if adjacent:
                    elf_killed = do_attack(adjacent, elves, 3)
                    if elf_killed:
                        # print("Elf killed")
                        elves_killed += 1

            if not elves or not goblins:
                if (pos, race) != order[~0]:
                    # Round not finished
                    round_finished = False
                break
        if round_finished:
            i += 1
        # print_board(grid, elves, goblins, i)
        if not elves or not goblins:
            break
    winners = goblins if goblins else elves
    # print(f"Elves killed = {elves_killed}")
    return i * sum(winners.values()), elves_killed


def do_attack(adjacent, enemies, damage):
    lowest = 100000
    targets = []
    for enemy in adjacent:
        if enemies[enemy] < lowest:
            lowest = enemies[enemy]
            targets = [enemy]
        elif enemies[enemy] == lowest:
            targets.append(enemy)
    # Sort choices based on reading order
    targets.sort(key=lambda x: x[0])
    targets.sort(key=lambda x: x[1])
    target = targets[0]

    enemies[target] -= damage
    if enemies[target] <= 0:
        del enemies[target]
        return True
    return False


def gross_possibles(elves, goblins, grid, is_elves):
    enemy = goblins if is_elves else elves

    possible_spaces = set()
    for pos, g in enemy.items():
        for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            npos = (pos[0] + x, pos[1] + y)
            if npos[0] >= len(grid[0]) or npos[0] <= 0:
                continue
            if npos[1] >= len(grid) or npos[1] <= 0:
                continue
            if grid[npos[1]][npos[0]] == "#":
                continue
            if npos in elves or npos in goblins:
                continue
            possible_spaces.add(npos)
    return possible_spaces


assert solve(EXAMPLE_1)[0] == 27730
assert solve(EXAMPLE_2)[0] == 36334
assert solve(EXAMPLE_3)[0] == 39514
assert solve(EXAMPLE_4)[0] == 27755
assert solve(EXAMPLE_5)[0] == 28944
assert solve(EXAMPLE_6)[0] == 18740

# 243390
print(f"Part 1: {solve(PUZZLE_INPUT)[0]}")

assert solve(EXAMPLE_1, 15) == (4988, 0)
assert solve(EXAMPLE_3, 4) == (31284, 0)
assert solve(EXAMPLE_4, 15) == (3478, 0)
assert solve(EXAMPLE_5, 12) == (6474, 0)
assert solve(EXAMPLE_6, 34) == (1140, 0)

damage = 4

while True:
    score, deaths = solve(PUZZLE_INPUT, damage)
    if deaths == 0:
        # 59886
        print(f"Part 2: {score}")
        break
    damage += 1
