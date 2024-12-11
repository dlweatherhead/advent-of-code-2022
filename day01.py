# --- Day 1: Calorie Counting ---
# https://adventofcode.com/2022/day/1

def get_elf_inventory_from_file(filename):
    f = open(filename, "r")
    groups = f.read().split("\n\n")

    elves = []
    for group in groups:
        elf = []
        for line in group.splitlines():
            elf.append(int(line))
        elves.append(elf)
    return elves


def determine_elf_with_max_calories(inventory):
    result = (-1, 0)
    for index, items in enumerate(inventory):
        total = sum(items)
        if total > result[1]:
            result = (index, total)
    return result


def get_top_elves(count, inventory):
    result = []
    for i in range(count):
        max_calories = determine_elf_with_max_calories(inventory)
        result.append(max_calories)
        del inventory[max_calories[0]]
    return result


def get_total_for_top_elves(count, inventory):
    top_elves = get_top_elves(count, inventory)
    total = 0
    for elf in top_elves:
        total += elf[1]
    return total


if __name__ == '__main__':

    # Puzzle 1
    print(get_total_for_top_elves(1, get_elf_inventory_from_file("day01_puzzle.txt")))

    # Puzzle 2
    print(get_total_for_top_elves(3, get_elf_inventory_from_file("day01_puzzle.txt")))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
