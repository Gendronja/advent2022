'''

A/X = ROCK
B/Y = PAPER
C/Z = SCISSORS

'''

play_score = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

play_dict = {
    "A": "X",
    "B": "Y",
    "C": "Z"
}

def readInput():
    f = open("input.txt", "r")
    lines = f.readlines()

    return lines

def checkWin(you, opponent):
    win_status = False

    if you == "X" and opponent == "C":
            win_status = True

    elif you == "Y" and opponent == "A":
        win_status = True

    elif you == "Z" and opponent == "B":
        win_status = True

    return win_status

def computeScore(lines):
    score = 0
    for line in lines:
        opponent = line[0]
        you = line[2]
        score += play_score[you]

        if you == play_dict[opponent]:
            score += 3
        elif checkWin(you, opponent):
            score += 6
    
    return score

def main():
    lines = readInput()
    score = computeScore(lines)
    print(score)


if __name__=="__main__":
    main()