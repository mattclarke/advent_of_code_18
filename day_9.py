class Marble:
    def __init__(self, value, prev, next):
        self.value = value
        self.next = next
        self.prev = prev


num_players = 424
players = [0] * num_players
num_marbles = 7114400

current = Marble(0, None, None)
current.prev = current
current.next = current
zeroth = current


def print_board():
    output ="{} ".format(zeroth.value)
    curr = zeroth.next
    while curr is not zeroth:
        if curr == current:
            output += "({}) ".format(curr.value)
        else:
            output += "{} ".format(curr.value)
        curr = curr.next
    print(output)


# Part 1 and 2
for i in range(num_marbles):
    player = i % num_players
    # print(player)

    if (i + 1) % 23 == 0:
        players[player] += i + 1
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
        new_marble = Marble(i+1, current, current.next)
        current.next.prev = new_marble
        current.next = new_marble
        current = new_marble
    # print_board()

print(max(players))


