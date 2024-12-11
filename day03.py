# --- Day 3: Rucksack Reorganization ---
# https://adventofcode.com/2022/day/3

def get_value_item(item):
    value = ord(item)
    if value >= 97:
        return value - 97 + 1
    if value >= 65:
        return value - 65 + 27


def split_rucksack(items):
    return items[:len(items)//2], items[len(items)//2:]


def find_common_items_in_rucksacks(items):
    rucksack = split_rucksack(items)
    common_items = []
    for left in rucksack[0]:
        for right in rucksack[1]:
            if left == right:
                common_items.append(left)
    return common_items


def get_values_of_items(items):
    total = 0
    for item in items:
        total += get_value_item(item)
    return total


def get_common_item_in_elf_group(elf_group):
    common_items = []
    for x in elf_group[0]:
        for y in elf_group[1]:
            for z in elf_group[2]:
                if x == y == z:
                    common_items.append(x)
    return common_items


filename = "day03_puzzle.txt"
f = open(filename, "r")
lines = f.read().split("\n")

sum = 0
for line in lines:
    common_items = find_common_items_in_rucksacks(line)
    items_value = get_values_of_items(dict.fromkeys(common_items))
    sum += items_value

print(sum)


elf_groups = []
i = 0
while i < len(lines):
    elf_groups.append((lines[i], lines[i+1], lines[i+2]))
    i += 3

sum = 0
for elf_group in elf_groups:
    common_items = get_common_item_in_elf_group(elf_group)
    items_value = get_values_of_items(dict.fromkeys(common_items))
    sum += items_value

print(sum)
