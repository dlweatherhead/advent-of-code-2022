# --- Day 6: Tuning Trouble ---
# https://adventofcode.com/2022/day/6

filename = "day06_puzzle.txt"
f = open(filename, "r")
datastream = f.read()

dsSample = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
ds1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"
ds2 = "nppdvjthqldpwncqszvftbrmjlhg"
ds3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
ds4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"


def does_duplicate_exist(sequence):
    for x in range(0, len(sequence)):
        for y in range(0, len(sequence)):
            if x == y:
                continue
            if sequence[x] == sequence[y]:
                return True
    return False


def find_marker(stream):
    for i in range(14, len(stream)):
        snip = stream[i-14:i]
        dupe = does_duplicate_exist(snip)
        if not dupe:
            return i
    return -1


print(find_marker(dsSample), " exp 7")
print(find_marker(ds1), " exp 5")
print(find_marker(ds2), " exp 6")
print(find_marker(ds3), " exp 10")
print(find_marker(ds4), " exp 11")
print(find_marker(datastream), " exp ?")



