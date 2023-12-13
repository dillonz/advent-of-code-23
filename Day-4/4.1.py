import math

input = open("input.txt", "r")
runningTotal = 0

while True:
    # Get each line and break if blank
    line = input.readline()
    if not line:
        break

    matches = 0

    allNums = line.split(": ")[1]
    [winningNumsStr, ownedNumsStr] = allNums.split('|')
    winningNums = set(winningNumsStr.split())
    ownedNums = ownedNumsStr.split()

    for num in ownedNums:
        if num in winningNums:
            matches += 1
    if matches > 0:
        runningTotal += math.pow(2, matches - 1)

print(runningTotal)
input.close()