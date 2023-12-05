input = open("input.txt", "r")
runningTotal = 0

maxValues = {
    'red': 12,
    'green': 13,
    'blue': 14
}
while True:
    # Get each line and break if blank
    line = input.readline()
    if not line:
        break
    
    # Get Game ID
    colonLoc = line.find(':')
    gameID = line[5:colonLoc]
    
    # Loop through each handful
    curIxStart = colonLoc + 1
    illegal = False
    while not illegal:
        handfulEnd = line.find(';', curIxStart)
        last = False
        if handfulEnd < 0:
            last = True
            handfulEnd = len(line)
        handful = line[curIxStart+1:handfulEnd]
        # Loop through each color in game
        handfulList = handful.split(', ')
        for colorGroup in handfulList:
            [num, color] = colorGroup.split()
            if (int(num) > maxValues[color]):
                illegal = True
        if last:
            break
        curIxStart = handfulEnd + 1
    if not illegal:
        runningTotal += int(gameID)

print(runningTotal)
input.close()