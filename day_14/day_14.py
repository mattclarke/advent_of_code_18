def print_board(recipes, a, b):
    line = ""
    for i, r in enumerate(recipes):
        if i == a:
            line += f"({r})"
        elif i == b:
            line += f"[{r}]"
        else:
            line += f" {r} "
    print(line)


elf_1 = 0
elf_2 = 1

recipes = [3, 7]
PUZZLE_INPUT = 513401   # number of recipes

# print_board(recipes, elf_1, elf_2)

while len(recipes) <= PUZZLE_INPUT + 10:
    # Add new recipes
    new_val = recipes[elf_1] + recipes[elf_2]
    val_1 = new_val // 10
    val_2 = new_val % 10
    if val_1 > 0:
        recipes.append(val_1)
    recipes.append(val_2)

    # Move elves
    elf_1 = (elf_1 + 1 + recipes[elf_1]) % len(recipes)
    elf_2 = (elf_2 + 1 + recipes[elf_2]) % len(recipes)

    # print_board(recipes, elf_1, elf_2)

ans = ""
for i in range(10):
    ans += "{}".format(recipes[PUZZLE_INPUT + i])

# 5371393113
print(f"Part 1: {ans}")

# Part 2
# Answer = 20286858
elf_1 = 0
elf_2 = 1

recipes = [3, 7]
puzzle_input = f"{PUZZLE_INPUT}"

output = "37"
count = 2

while True:
    if output != puzzle_input[: len(output)]:
        output = ""

    # Add new recipes
    new_val = recipes[elf_1] + recipes[elf_2]
    val_1 = new_val // 10
    val_2 = new_val % 10
    if val_1 > 0:
        recipes.append(val_1)
        count += 1
        if output + str(val_1) == puzzle_input[: len(output) + 1]:
            output += str(val_1)
        else:
            output = ""
        if puzzle_input in output:
            # print_board(recipes[-10:], 0, 0)
            print(f"Part 2: {len(recipes) - len(puzzle_input)}")
            break
    recipes.append(val_2)
    count += 1
    if output + str(val_2) == puzzle_input[: len(output) + 1]:
        output += str(val_2)
    else:
        output = ""

    # Move elves
    elf_1 = (elf_1 + 1 + recipes[elf_1]) % len(recipes)
    elf_2 = (elf_2 + 1 + recipes[elf_2]) % len(recipes)

    # if len(output) >= 5:
    #     print(output)
    # print_board(recipes, elf_1, elf_2)
    if puzzle_input in output:
        print_board(recipes[-10:], 0, 0)
        print(f"Part 2: {len(recipes) - len(puzzle_input)}")
        break
