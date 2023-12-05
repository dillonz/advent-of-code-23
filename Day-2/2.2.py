input = open("input.txt", "r")
runningTotal = 0

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
    maxValues = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    while True:
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
                maxValues[color] = int(num)
        if last:
            runningTotal += maxValues['red'] * maxValues['green'] * maxValues['blue']
            break
        curIxStart = handfulEnd + 1

print(runningTotal)
input.close()