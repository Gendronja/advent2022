'''

A = ROCK
B = PAPER
C = SCISSORS

X = LOSE
Y = DRAW
Z = WIN

'''

import itertools

play_score = {
    "A": 1,
    "B": 2,
    "C": 3
}

lose_dict = {
    "A": "C",
    "B": "A",
    "C": "B"
}

draw_dict = {
    "A": "A",
    "B": "B",
    "C": "C"
}

win_dict = {
    "A": "B",
    "B": "C",
    "C": "A"
}

def readInput():
    f = open("input.txt", "r")
    lines = f.readlines()

    return lines


def computeEnd(opponent, round_end):
    if round_end == "X":
        you = lose_dict[opponent]
    elif round_end == "Y":
        you = draw_dict[opponent]
    elif round_end == "Z":
        you = win_dict[opponent]

    return you


def computePlays(lines):
    plays = []
    for line in lines:
        opponent = line[0]
        round_end = line[2]

        you = computeEnd(opponent, round_end)
        plays.append(you)

    return plays


def computeScore(lines, plays):
    score = 0
    for line,you in zip(lines,plays):
            
            score += play_score[you]
            win_status = line[2]
            if win_status == "Y":
                score += 3
            elif win_status == "Z":
                score += 6
    
    return score

def main():
    lines = readInput()
    plays = computePlays(lines)
    score = computeScore(lines, plays)
    print(score)


if __name__=="__main__":
    main()