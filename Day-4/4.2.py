import math

input = open("input.txt", "r")
runningTotal = 0

earnedExtras = {}

lineNum = 0
while True:
    # Get each line and break if blank
    line = input.readline()
    if not line:
        break
    lineNum += 1

    totalOfCard = 1
    if lineNum in earnedExtras:
        totalOfCard += earnedExtras[lineNum]

    runningTotal += totalOfCard
    matches = 0

    allNums = line.split(": ")[1]
    [winningNumsStr, ownedNumsStr] = allNums.split('|')
    winningNums = set(winningNumsStr.split())
    ownedNums = ownedNumsStr.split()

    for num in ownedNums:
        if num in winningNums:
            matches += 1
    if matches > 0:
        for i in range(lineNum + 1, lineNum + matches + 1):
            if i not in earnedExtras:
                earnedExtras[i] = 0
            earnedExtras[i] += totalOfCard
print(runningTotal)
input.close()