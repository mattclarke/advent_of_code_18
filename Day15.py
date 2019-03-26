real_data = """
################################
#########....#..#####.......####
###########G......###..##..#####
###########.....#.###......#####
###############.#...#.......####
###############..#....E......###
############.##...#...G....#####
############.##.....G..E...#####
###########G.##...GG......######
#..####G##..G##..G.#......######
#..........#............#.######
#.......#....G.......G.##..#...#
#.....G.......#####...####...#.#
#.....G..#...#######..#####...E#
#.##.....G..#########.#######..#
#........G..#########.#######E##
####........#########.##########
##.#........#########.##########
##.G....G...#########.##########
##...........#######..##########
#.G..#........#####...##########
#......#.G.G..........##########
###.#................###########
###..................###.#######
####............E.....#....#####
####.####.......####....E.######
####..#####.....####......######
#############..#####......######
#####################EE..E######
#####################..#.E######
#####################.##########
################################
"""


raw_data_v1= """
#######
#E..G.#
#...#.#
#.G.#G#
#######
"""

raw_data_v2= """
#######
#.E...#
#.....#
#...G.#
#######
"""

raw_data_v3= """
#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########
"""

raw_data_v4 = """
#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######
"""

raw_data_v5 = """
#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######
"""

raw_data_v6 = """
#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######
"""

raw_data_v7 = """
#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######
"""

raw_data_v8 = """
#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######
"""

raw_data_v9 = """
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


raw_data = real_data


class Square:
    def __init__(self, pos, content=None):
        self.content = content
        self.pos = pos

    def __str__(self):
        if self.content is None:
            return "."
        elif isinstance(self.content, Goblin):
            return "G"
        elif isinstance(self.content, Elf):
            return "E"
        elif isinstance(self.content, Wall):
            return "#"
        else:
            raise Exception("Content error!")


class Goblin:
    def __init__(self, pos):
        self.pos = pos
        self.moved = False
        self.attack = 3
        self.hit_points = 200


class Elf:
    def __init__(self, pos):
        self.pos = pos
        self.moved = False
        self.attack = 3
        self.hit_points = 200


class Wall:
    pass


class ElfDeath(Exception):
    pass


max_x = 0
max_y = 0

# Quickly find dimenstions of board
for line in raw_data.splitlines():
    if not line:
        continue
    for x, c in enumerate(line):
        max_x = max(len(line), max_x)
    max_y += 1

board = [[None for y in range(max_y)] for x in range(max_x)]
elves = []
goblins = []


def create_board():
    global board, elves, goblins

    board = [[None for y in range(max_y)] for x in range(max_x)]
    elves = []
    goblins = []

    y = 0

    for line in raw_data.splitlines():
        if not line:
            continue
        for x, c in enumerate(line):
            content = None
            if c == "#":
                content = Wall()
            elif c == "G":
                content = Goblin([x, y])
                goblins.append(content)
            elif c == "E":
                content = Elf([x, y])
                elves.append(content)
            board[x][y] = Square([x,y], content)
        y += 1


def print_board(board, moves=None):
    for j in range(len(board[0])):
        line = ""
        for i in range(len(board)):
            if moves is None:
                line += "{}".format(str(board[i][j]))
            else:
                if board[i][j] in moves and board[i][j].content is None:
                    line += "?"
                else:
                    line += "{}".format(str(board[i][j]))
        print(line)


def get_valid_moves(board, pos):
    def _helper(result):
        if result.content is not None:
            if isinstance(result.content, Goblin):
                return result.content
            elif isinstance(result.content, Elf):
                return result.content
            else:
                return "#"
        return result

    # Top, left, right, bottom
    top = board[pos[0]][pos[1] - 1]
    top = _helper(top)

    left = board[pos[0] - 1][pos[1]]
    left = _helper(left)

    right = board[pos[0] + 1][pos[1]]
    right = _helper(right)

    bottom = board[pos[0]][pos[1] + 1]
    bottom = _helper(bottom)

    return [top, left, right, bottom]


def get_reachable(board, start_square):
    if isinstance(start_square.content, Elf):
        is_elf = True
    else:
        is_elf = False

    painted = {start_square}
    reachable = set()
    full = False
    while not full:
        full = True
        to_add = []
        for p in painted:
            valid = get_valid_moves(board, p.pos)
            for v in valid:
                if isinstance(v, Goblin):
                    if is_elf:
                        reachable.add(p)
                elif isinstance(v, Elf):
                    if not is_elf:
                        reachable.add(p)
                elif v is not "#" and v not in painted:
                    to_add.append(v)
                    full = False
        painted.update(to_add)
    return reachable


def get_closest(start_square, reachable):
    if isinstance(start_square.content, Elf):
        is_elf = True
    else:
        is_elf = False

    p_board = [[None for y in range(max_y)] for x in range(max_x)]
    p_board[start_square.pos[0]][start_square.pos[1]] = 0

    painted = {start_square}
    full = False
    while not full:
        full = True
        to_add = []
        for p in painted:
            score = p_board[p.pos[0]][p.pos[1]]
            valid = get_valid_moves(board, p.pos)
            for v in valid:
                if isinstance(v, Goblin):
                    pass
                elif isinstance(v, Elf):
                    pass
                elif v is not "#":
                    if p_board[v.pos[0]][v.pos[1]] is None:
                        p_board[v.pos[0]][v.pos[1]] = score + 1
                    elif score + 1 < p_board[v.pos[0]][v.pos[1]]:
                        p_board[v.pos[0]][v.pos[1]] = score + 1
                    else:
                        continue
                    to_add.append(v)
                    full = False
        painted.update(to_add)
    # print_path_board(p_board)
    closet = None
    dist = float("inf")
    for r in reachable:
        if p_board[r.pos[0]][r.pos[1]] < dist:
            closet = r
            dist = p_board[r.pos[0]][r.pos[1]]
        elif p_board[r.pos[0]][r.pos[1]] == dist:
            # Choose based on reading order
            if r.pos[1] < closet.pos[1]:
                closet = r
            elif r.pos[1] == closet.pos[1] and r.pos[0] < closet.pos[0]:
                closet = r
    return closet


def get_possible_paths(board, start, end):
    p_board = [[None for y in range(max_y)] for x in range(max_x)]
    p_board[end.pos[0]][end.pos[1]] = 0

    painted = {end}
    full = False
    while not full:
        full = True
        to_add = []
        for p in painted:
            score = p_board[p.pos[0]][p.pos[1]]
            valid = get_valid_moves(board, p.pos)
            for v in valid:
                if isinstance(v, Goblin):
                    pass
                elif isinstance(v, Elf):
                    pass
                elif v is not "#":
                    if p_board[v.pos[0]][v.pos[1]] is None:
                        p_board[v.pos[0]][v.pos[1]] = score + 1
                    elif score + 1 < p_board[v.pos[0]][v.pos[1]]:
                        p_board[v.pos[0]][v.pos[1]] = score + 1
                    else:
                        continue
                    to_add.append(v)
                    full = False
        painted.update(to_add)
    return p_board


def print_path_board(board):
    for j in range(len(board[0])):
        line = ""
        for i in range(len(board)):
            if board[i][j] is None:
                line += "    "
            else:
                if len(str(board[i][j])) == 1:
                    line += " {}  ".format(str(board[i][j]))
                else:
                    line += " {} ".format(str(board[i][j]))
        print(line)


def pick_direction(paths, elf_sq):
    lowest = float("inf")
    direction = None
    up = paths[elf_sq.pos[0]][elf_sq.pos[1] - 1]
    if up is not None:
        lowest = up
        direction = (0, -1)

    left = paths[elf_sq.pos[0] - 1][elf_sq.pos[1]]
    if left is not None:
        if left < lowest:
            lowest = left
            direction = (-1, 0)

    right = paths[elf_sq.pos[0] + 1][elf_sq.pos[1]]
    if right is not None:
        if right < lowest:
            lowest = right
            direction = (1, 0)

    down = paths[elf_sq.pos[0]][elf_sq.pos[1] + 1]
    if down is not None:
        if down < lowest:
            lowest = down
            direction = (0, 1)

    if direction is None:
        raise Exception("Something up with direction")

    return direction


def do_move(board, elf_sq, direction):
    new_sq = board[elf_sq.pos[0] + direction[0]][elf_sq.pos[1] + direction[1]]
    new_sq.content = elf_sq.content
    elf_sq.content = None
    new_sq.content.pos = new_sq.pos
    new_sq.content.moved = True
    return new_sq


def do_attack(board, square, is_elf):
    moves = get_valid_moves(board, square.pos)
    if is_elf:
        # Take a swing at a goblin if possible
        opponents = [g for g in moves if isinstance(g, Goblin)]
        if opponents:
            weakest = opponents[0]
            hp = opponents[0].hit_points
            for op in opponents:
                if op.hit_points < hp:
                    weakest = op
                    hp = op.hit_points

            # Hit the weakest
            weakest.hit_points -= square.content.attack
            if weakest.hit_points < 1:
                # Killed
                board[weakest.pos[0]][weakest.pos[1]].content = None
                goblins.remove(weakest)

            return True
    elif not is_elf:
        # Take a swing at an elf
        opponents = [e for e in moves if isinstance(e, Elf)]
        if opponents:
            weakest = opponents[0]
            hp = opponents[0].hit_points
            for op in opponents:
                if op.hit_points < hp:
                    weakest = op
                    hp = op.hit_points

            # Hit the weakest
            weakest.hit_points -= square.content.attack
            if weakest.hit_points < 1:
                # Killed
                # Comment out for part 1
                raise ElfDeath("Oops")

                board[weakest.pos[0]][weakest.pos[1]].content = None
                elves.remove(weakest)

            return True

    return False


def do_action(board, square, is_elf):
    # Check for hittable
    hit = do_attack(board,square,is_elf)
    if hit:
        return

    reachable = get_reachable(board, square)
    # print_board(board, reachable)

    if not reachable:
        return

    closest = get_closest(square, reachable)
    # print_board(board, [closest])

    paths = get_possible_paths(board, square, closest)
    # print_path_board(paths)

    direction = pick_direction(paths, square)
    # print(direction)

    square = do_move(board, square, direction)
    # print_board(board)

    # Check for hittable
    hit = do_attack(board, square, is_elf)


def do_turn(board):
    completed = True
    for j in range(max_y):
        for i in range(max_x):
            if isinstance(board[i][j].content, Elf) or isinstance(board[i][j].content, Goblin):
                if not board[i][j].content.moved:
                    if len(elves) == 0 or len(goblins) == 0:
                        completed = False
                    do_action(board, board[i][j], isinstance(board[i][j].content, Elf))
                    # print_board(board)

    for g in goblins:
        g.moved = False
    for e in elves:
        e.moved = False
    return completed


# Start game
def run_game(board, elf_power=3):
    for e in elves:
        e.attack = elf_power

    count = 0

    while True:
        # print_board(board)
        # for g in goblins:
        #     print("G({})".format(g.hit_points))
        # for e in elves:
        #     print("E({})".format(e.hit_points))
        if do_turn(board):
            count += 1

        # Check to see if finished
        if len(elves) == 0 or len(goblins) == 0:
            print_board(board)
            break

    print(count)

    total_hp = 0
    for e in elves:
        total_hp += e.hit_points
    for g in goblins:
        total_hp += g.hit_points

    print(total_hp)
    print(count * total_hp)


# Part 1
# create_board()
# run_game(board)

# Part 2
# Binary search
low = 0
high = 50

while low != high and low + 1 != high:
    passed = True
    aim = low + (high - low) // 2
    print(f"Aim: {aim}")

    try:
        create_board()
        run_game(board, aim)
    except ElfDeath as err:
        print("FAIL")
        low = aim
        continue
    high = aim

# Answer is 48,790 but that is rejected
# I have confirmed this will the online version https://lamperi.name/aoc/







