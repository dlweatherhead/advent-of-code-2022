# --- Day 4: Camp Cleanup ---
# https://adventofcode.com/2022/day/4

def does_fully_contain(left, right):
    if left[0] >= right[0] and left[1] <= right[1]:
        return True
    if right[0] >= left[0] and right[1] <= left[1]:
        return True
    return False


def does_partially_contain(left, right):
    if right[0] <= left[0] <= right[1]:
        return True
    if right[0] <= left[1] <= right[1]:
        return True
    if left[0] <= right[0] <= left[1]:
        return True
    if left[1] <= right[1] <= left[1]:
        return True
    return False


filename = "day04_puzzle.txt"
f = open(filename, "r")
lines = f.read().split("\n")

full_overlaps = 0
partial_overlaps = 0
for line in lines:
    pair = line.split(",")
    pair_left = pair[0].split("-")
    pair_right = pair[1].split("-")
    left = (int(pair_left[0]), int(pair_left[1]))
    right = (int(pair_right[0]), int(pair_right[1]))
    if does_fully_contain(left, right):
        full_overlaps += 1
    if does_partially_contain(left, right):
        partial_overlaps += 1

print("Fully overlapped")
print(full_overlaps)
print("Partially overlapped")
print(partial_overlaps)
