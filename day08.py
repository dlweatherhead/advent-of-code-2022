# --- Day 8: Treetop Tree House ---
# https://adventofcode.com/2022/day/8

filename = "day08_puzzle.txt"

f = open(filename, "r")
lines = f.read().split("\n")

map = []
for a in lines:
    inner = []
    for b in a:
        inner.append(int(b))
    map.append(inner)
print(map)

col_len = len(map)
row_len = len(map[0])

outer_count = (2 * row_len) + (2 * (col_len - 2))
print(outer_count)


def any_larger_x(index_x, index_y, start, end):
    larger = False
    for x in range(start, end):
        if map[index_y][x] >= map[index_y][index_x]:
            larger = True
            break
    return larger


def any_larger_y(index_x, index_y, start, end):
    larger = False
    for y in range(start, end):
        if map[y][index_x] >= map[index_y][index_x]:
            larger = True
            break
    return larger


def part_1():
    visible_count = 0
    for xx in range(1, col_len - 1):
        for yy in range(1, row_len - 1):
            # row
            left = any_larger_x(xx, yy, 0, xx)
            right = any_larger_x(xx, yy, xx + 1, row_len)

            # col
            top = any_larger_y(xx, yy, 0, yy)
            bottom = any_larger_y(xx, yy, yy + 1, col_len)

            if not (left and right and top and bottom):
                visible_count += 1

    print(visible_count)
    print(visible_count + outer_count)


def get_sight_count_left(index_x, index_y, start, end):
    count = 0
    for x in reversed(range(start, end)):
        count += 1
        if map[index_y][x] >= map[index_y][index_x]:
            break
    return count


def get_sight_count_right(index_x, index_y, start, end):
    count = 0
    for x in range(start, end):
        count += 1
        if map[index_y][x] >= map[index_y][index_x]:
            break
    return count


def get_sight_count_top(index_x, index_y, start, end):
    count = 0
    for y in reversed(range(start, end)):
        count += 1
        if map[y][index_x] >= map[index_y][index_x]:
            break
    return count


def get_sight_count_bottom(index_x, index_y, start, end):
    count = 0
    for y in range(start, end):
        count += 1
        if map[y][index_x] >= map[index_y][index_x]:
            break
    return count


def part_2():
    highest_scenic_score = 0
    for xx in range(1, col_len - 1):
        for yy in range(1, row_len - 1):
            # row
            left = get_sight_count_left(xx, yy, 0, xx)
            right = get_sight_count_right(xx, yy, xx + 1, row_len)

            # col
            top = get_sight_count_top(xx, yy, 0, yy)
            bottom = get_sight_count_bottom(xx, yy, yy + 1, col_len)

            scenic_score = left * right * top * bottom

            print(xx, yy, ":", left, right, top, bottom, scenic_score)

            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    print(highest_scenic_score)


part_2()
