


def readCalories():
    f = open("input.txt", "r")
    lines = f.readlines()
    elf_calories = [0]
    i = 0
    for line in lines:
        if line == '\n':
            i = i + 1
            elf_calories.append(0)
        else:
            elf_calories[i] = elf_calories[i] + int(line)

    return elf_calories

def reportTopThree(elf_calories):
    elf_calories.sort(reverse=True)
    top_three = elf_calories[0] + elf_calories[1] + elf_calories[2]

    return top_three

if __name__=="__main__":
    elf_calories = readCalories()
    top_three = reportTopThree(elf_calories)
    print(top_three)