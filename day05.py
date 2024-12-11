# --- Day 5: Supply Stacks ---
# https://adventofcode.com/2022/day/5
from array import *

filename = "day05_puzzle.txt"
commands_start = 11

f = open(filename, "r")
lines = f.read().split("\n")


# PARSE THE STACKS
n = 4
stack_input = []
for stack_line in lines[:commands_start-2]:
    stack_set = [stack_line[i:i + n].strip() for i in range(0, len(stack_line), n)]
    stack_input.append(stack_set)


def parse_stacks():
    stack_count = len(stack_input[len(stack_input)-1])
    stacks = [[] * stack_count for i in range(stack_count)]

    index = len(stack_input)-1
    while index >= 0:
        line = stack_input[index]
        for x in range(0, len(line)):
            if line[x] != '':
                stacks[x].append(line[x])
        index -= 1
    return stacks


# PARSE THE MOVE SETS
def parse_move_sets():
    move_set = []
    for cmd in lines[commands_start-1:]:
        qty = int(cmd.split("move ")[1].split(" ")[0])
        start = int(cmd.split("from ")[1].split(" ")[0])
        end = int(cmd.split("to ")[1])
        move_set.append((qty, start, end))
    return move_set


def apply_moves():
    for move in move_sets:
        amount = move[0]
        from_stack = move[1] - 1
        to_stack = move[2] - 1
        while amount > 0:
            if len(stacks[from_stack]) > 0:
                item = stacks[from_stack].pop()
                stacks[to_stack].append(item)
            amount -= 1
    return stacks


def apply_moves_in_order():
    for move in move_sets:
        amount = move[0]
        from_stack = move[1] - 1
        to_stack = move[2] - 1
        if len(stacks[from_stack]) > 0:
            items = stacks[from_stack][-amount:]
            stacks[from_stack] = stacks[from_stack][-amount:]
            stacks[to_stack].extend(items)
        print(str(move) + " -> " + str(stacks))
    return stacks


def apply_moves_full_stack_pop():
    for move in move_sets:
        counter = 0
        amount = move[0]
        from_stack = move[1] - 1
        to_stack = move[2] - 1
        while counter < amount:
            if len(stacks[from_stack]) > 0:
                item = stacks[from_stack].pop(len(stacks[from_stack]) - amount + counter)
                stacks[to_stack].append(item)
            counter += 1
    return stacks


stacks = parse_stacks()
print(stacks)
move_sets = parse_move_sets()
apply_moves_full_stack_pop()
print(stacks)

last_item_line = ""
for stack in stacks:
    last_item = stack[len(stack)-1]
    last_item_line += last_item[1]
    print(last_item)

print(last_item_line)
