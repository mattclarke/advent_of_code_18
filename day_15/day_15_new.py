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


def print_board(grid, elves, goblins, round):
    print(f"After {round} rounds:")
    y = len(grid)
    for y, row in enumerate(grid):
        line = []
        extra = []
        for x in range(len(row)):
            if (x, y) in elves:
                line.append("E")
                extra.append(f"E({elves[(x,y)]})")
            elif (x, y) in goblins:
                line.append("G")
                extra.append(f"G({goblins[(x, y)]})")
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
    order = list(elves.keys())
    order.extend(goblins.keys())
    order.sort(key=lambda x: x[0])
    order.sort(key=lambda x: x[1])
    return order


def find_closest(origin, grid, elves, goblins,  possibles):
    queue = [[origin]]
    solutions = []
    lowest = 1000000000
    visited = {
        origin: 0
    }

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


def solve(starting_grid):
    grid, elves, goblins = process_input(starting_grid)
    print_board(grid, elves, goblins, 0)
    i = 0
    while True:
        round_finished = True
        order = calculate_move_order(elves, goblins)
        for pos in order:
            if pos in elves:
                adjacent = get_adjacent(pos, goblins)
                if not adjacent:
                    possible_spaces = gross_possibles(elves, goblins, grid, True)
                    possible_routes = find_closest(pos, grid, elves, goblins, possible_spaces)
                    possible_routes.sort(key=lambda x: x[0])
                    possible_routes.sort(key=lambda x: x[1])
                    if possible_routes:
                        choice = possible_routes[0]

                        hp = elves[pos]
                        del elves[pos]
                        elves[choice] = hp
                        adjacent = get_adjacent(choice, goblins)

                if adjacent:
                    do_attack(adjacent, goblins, 3)
            elif pos in goblins:
                adjacent = get_adjacent(pos, elves)
                if not adjacent:
                    possible_spaces = gross_possibles(elves, goblins, grid, False)
                    possible_routes = find_closest(pos, grid, elves, goblins,
                                                   possible_spaces)
                    possible_routes.sort(key=lambda x: x[0])
                    possible_routes.sort(key=lambda x: x[1])
                    if possible_routes:
                        choice = possible_routes[0]

                        hp = goblins[pos]
                        del goblins[pos]
                        goblins[choice] = hp
                        adjacent = get_adjacent(choice, elves)

                if adjacent:
                    do_attack(adjacent, elves, 3)

            if not elves or not goblins:
                if pos != order[~0]:
                    # Round not finished
                    round_finished = False
                break
        if round_finished:
            i += 1
        print_board(grid, elves, goblins, i)
        if not elves or not goblins:
            break
    winners = goblins if goblins else elves
    return i * sum(winners.values())


def do_attack(adjacent, enemies, damage):
    lowest = 100000
    targets = []
    for enemy in adjacent:
        if enemies[enemy] < lowest:
            lowest = enemies[enemy]
            targets=[enemy]
        elif enemies[enemy] == lowest:
            targets.append(enemy)
    # Sort choices based on reading order
    targets.sort(key=lambda x: x[0])
    targets.sort(key=lambda x: x[1])
    target = targets[0]

    enemies[target] -= damage
    if enemies[target] <= 0:
        del enemies[target]


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


# assert solve(EXAMPLE_1) == 27730
# assert solve(EXAMPLE_2) == 36334
# assert solve(EXAMPLE_3) == 39514
# assert solve(EXAMPLE_4) == 27755
# assert solve(EXAMPLE_5) == 28944
# assert solve(EXAMPLE_6) == 18740

print(f"Part 1: {solve(PUZZLE_INPUT)}")
