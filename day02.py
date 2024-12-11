# --- Day 2: Rock Paper Scissors ---
# # https://adventofcode.com/2022/day/2

# A=rock, B=paper, C=scissors
# X=rock, Y=paper, Z=scissors

def get_score_for_shape(player):
    if player == "X":
        return 1
    elif player == "Y":
        return 2
    elif player == "Z":
        return 3
    return 0


def get_score_for_result(player, opponent):
    if player == "X" and opponent == "C":
        return 6
    if player == "Y" and opponent == "A":
        return 6
    if player == "Z" and opponent == "B":
        return 6
    if player == "Z" and opponent == "A":
        return 0
    if player == "X" and opponent == "B":
        return 0
    if player == "Y" and opponent == "C":
        return 0
    return 3


def get_score_for_intended_outcome(outcome, opponent):
    if outcome == "Z":
        return 6
    if outcome == "Y":
        return 3
    return 0


def get_shape_score_for_opponent_and_outcoem(outcome, opponent):
    # rock=1, paper=2, scissors=3
    # rock -> lose=3, draw=1, win=2
    # paper -> lose=1, draw=2, win=3
    # scissors -> lose=2, draw=3, win=1
    if opponent == "A":
        if outcome == "X":
            return 3
        if outcome == "Y":
            return 1
        if outcome == "Z":
            return 2
    if opponent == "B":
        if outcome == "X":
            return 1
        if outcome == "Y":
            return 2
        if outcome == "Z":
            return 3
    if opponent == "C":
        if outcome == "X":
            return 2
        if outcome == "Y":
            return 3
        if outcome == "Z":
            return 1


def puzzle_1(lines):
    score = 0
    for line in lines:
        round = line.split(" ")
        score += get_score_for_shape(round[1])
        score += get_score_for_result(round[1], round[0])
    return score


def puzzle_2(lines):
    score = 0
    for line in lines:
        round = line.split(" ")
        score += get_score_for_intended_outcome(round[1], round[0])
        score += get_shape_score_for_opponent_and_outcoem(round[1], round[0])
    return score


filename = "day02_puzzle.txt"

f = open(filename, "r")
lines = f.read().split("\n")

print(puzzle_1(lines))
print(puzzle_2(lines))


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
