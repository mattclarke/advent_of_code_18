class Marble:
    def __init__(self, value, prev, next):
        self.value = value
        self.next = next
        self.prev = prev


def solve(part_2=False):
    num_players = 424
    players = [0] * num_players
    num_marbles = 7114400 if part_2 else 71144

    current = Marble(0, None, None)
    current.prev = current
    current.next = current
    zeroth = current

    def print_board():
        output = "{} ".format(zeroth.value)
        curr = zeroth.next
        while curr is not zeroth:
            if curr == current:
                output += "({}) ".format(curr.value)
            else:
                output += "{} ".format(curr.value)
            curr = curr.next
        print(output)

    for i in range(1, num_marbles + 1):
        player = i % num_players
        # print(player)

        if i % 23 == 0:
            players[player] += i
            for _ in range(7):
                current = current.prev
            # Remove marble
            # print("keeping {}".format(current.value))
            players[player] += current.value
            current.next.prev = current.prev
            current.prev.next = current.next
            current = current.next
        else:
            # Insert the marble 1 clockwise
            current = current.next
            new_marble = Marble(i, current, current.next)
            current.next.prev = new_marble
            current.next = new_marble
            current = new_marble
        # print_board()
    return players


# Part 1
players = solve()

# 405143
print(f"Part 1: {max(players)}")

# Part 2
players = solve(True)

# 3411514667
print(f"Part 2: {max(players)}")
