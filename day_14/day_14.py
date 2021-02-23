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
num_recipes = 513401

print_board(recipes, elf_1, elf_2)

while len(recipes) <= num_recipes + 10:
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
    ans += "{}".format(recipes[num_recipes + i])

print(ans)

# Part 2
elf_1 = 0
elf_2 = 1


import collections

# Use a deque, so don't have to keep reallocating space for a list
recipes = []
recipes.append(3)
recipes.append(7)
pinput = "513401"

output = "37"
count = 2

while True:
    if output != pinput[: len(output)]:
        output = ""

    # Add new recipes
    new_val = recipes[elf_1] + recipes[elf_2]
    val_1 = new_val // 10
    val_2 = new_val % 10
    if val_1 > 0:
        recipes.append(val_1)
        count += 1
        if output + str(val_1) == pinput[: len(output) + 1]:
            output += str(val_1)
        else:
            output = ""
        if pinput in output:
            print_board(recipes[-10:], 0, 0)
            print("Got it!", len(recipes) - len(pinput))
            break
    recipes.append(val_2)
    count += 1
    if output + str(val_2) == pinput[: len(output) + 1]:
        output += str(val_2)
    else:
        output = ""

    # Move elves
    elf_1 = (elf_1 + 1 + recipes[elf_1]) % len(recipes)
    elf_2 = (elf_2 + 1 + recipes[elf_2]) % len(recipes)

    if len(output) >= 5:
        print(output)
    # print_board(recipes, elf_1, elf_2)
    if pinput in output:
        print_board(recipes[-10:], 0, 0)
        print("Got it!", len(recipes) - len(pinput))
        break
