with open("input.txt") as f:
    PUZZLE_INPUT = f.read()


class TrackPiece:
    def __init__(self, type, x, y, cart=None):
        self.type = type
        self.x = x
        self.y = y
        self.cart = cart

    def __str__(self):
        if self.cart:
            return self.cart.dir
        else:
            return self.type


class Cart:
    def __init__(self, dir):
        self.dir = dir
        self.moved = False
        self.turn = "<"

    def update(self):
        if self.turn == "<":
            self.turn = "|"
        elif self.turn == "|":
            self.turn = ">"
        elif self.turn == ">":
            self.turn = "<"


def print_track(track, x_max, y_max):
    for j in range(y_max):
        line = ""
        for i in range(x_max + 1):
            key = (i, j)
            if key in track:
                line += str(track[key])
            else:
                line += " "
        print(line)


# Build track
track = {}
carts = []
y = 0
x_max = 1
y_max = 0

# Choose input data here
for line in PUZZLE_INPUT.splitlines():
    if not line:
        continue
    for x, p in enumerate(line):
        if p in ["|", "-", "/", "\\", "+"]:
            track[(x, y)] = TrackPiece(p, x, y)
        elif p == "v" or p == "^":
            c = Cart(p)
            carts.append(c)
            track[(x, y)] = TrackPiece("|", x, y, c)
        elif p == "<" or p == ">":
            c = Cart(p)
            carts.append(c)
            track[(x, y)] = TrackPiece("-", x, y, c)
        x_max = max(x, x_max)
    y += 1
    y_max = max(y, y_max)


# print_track(track, x_max, y_max)


part_1_solved = False


def move_cart(track, x, y):
    global part_1_solved
    key = (x, y)
    cart = track[key].cart
    cart.moved = True
    if cart.dir == "v":
        track[key].cart = None
        key = (x, y + 1)
        if track[key].cart:
            # Part 1 - first collision
            if not part_1_solved:
                print("Part 1: {}, {}".format(key[0], key[1]))
                part_1_solved = True
            # Part 2 - remove both carts
            carts.remove(cart)
            carts.remove(track[key].cart)
            track[key].cart = None
            return
        track[key].cart = cart
        if track[key].type == "\\":
            cart.dir = ">"
        elif track[key].type == "/":
            cart.dir = "<"
        elif track[key].type == "+":
            if cart.turn == "<":
                cart.dir = ">"
            elif cart.turn == ">":
                cart.dir = "<"
            # Do nothing for straight
            cart.update()
    elif cart.dir == "^":
        track[key].cart = None
        key = (x, y - 1)
        if track[key].cart:
            # Part 1 - first collision
            if not part_1_solved:
                print("Part 1: {}, {}".format(key[0], key[1]))
                part_1_solved = True
            # Part 2 - remove both carts
            carts.remove(cart)
            carts.remove(track[key].cart)
            track[key].cart = None
            return
        track[key].cart = cart
        if track[key].type == "\\":
            cart.dir = "<"
        elif track[key].type == "/":
            cart.dir = ">"
        elif track[key].type == "+":
            if cart.turn == "<":
                cart.dir = "<"
            elif cart.turn == ">":
                cart.dir = ">"
            # Do nothing for straight
            cart.update()
    elif cart.dir == ">":
        track[key].cart = None
        key = (x + 1, y)
        if track[key].cart:
            # Part 1 - first collision
            if not part_1_solved:
                print("Part 1: {}, {}".format(key[0], key[1]))
                part_1_solved = True
            # Part 2 - remove both carts
            carts.remove(cart)
            carts.remove(track[key].cart)
            track[key].cart = None
            return
        track[key].cart = cart
        if track[key].type == "\\":
            cart.dir = "v"
        elif track[key].type == "/":
            cart.dir = "^"
        elif track[key].type == "+":
            if cart.turn == "<":
                cart.dir = "^"
            elif cart.turn == ">":
                cart.dir = "v"
            # Do nothing for straight
            cart.update()
    elif cart.dir == "<":
        track[key].cart = None
        key = (x - 1, y)
        if track[key].cart:
            # Part 1 - first collision
            if not part_1_solved:
                print("Part 1: {}, {}".format(key[0], key[1]))
                part_1_solved = True
            # Part 2 - remove both carts
            carts.remove(cart)
            carts.remove(track[key].cart)
            track[key].cart = None
            return
        track[key].cart = cart
        if track[key].type == "\\":
            cart.dir = "^"
        elif track[key].type == "/":
            cart.dir = "v"
        elif track[key].type == "+":
            if cart.turn == "<":
                cart.dir = "v"
            elif cart.turn == ">":
                cart.dir = "^"
            # Do nothing for straight
            cart.update()


def update(track, x_max, y_max):
    # This is for part 2
    down_to_last = False
    if len(carts) == 1:
        down_to_last = True

    for j in range(y_max):
        for i in range(x_max + 1):
            key = (i, j)
            if key in track:
                if track[key].cart:
                    # This is for part 2
                    if down_to_last:
                        # 124, 103
                        print(f"Part 2 = {i}, {j}")
                        return True
                    if not track[key].cart.moved:
                        # Move cart
                        move_cart(track, i, j)
    return False


# Part 1 = 46, 18
# Part 2 = 124, 103

finished = False

while not finished:
    finished = update(track, x_max, y_max)
    for c in carts:
        c.moved = False
