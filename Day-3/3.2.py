input = open("input.txt", "r")
runningTotal = 0

# Numbers in the form of: 
# {
#   num: <number>, 
#   counted: <whether or not it's been counted as bool>
# }
arrOfNums = []

# Index of locations adjacent to a number in form of:
# { <x>: { <y>: [<list of indexes to arrOfNums] }}
# where numIx connects to arrOfNums
iOfLocs = {}

# Index of the other characters in form of:
# { "x": <x>, "y": <y> }
iOfRandomChars = []
def updateArrays(number, endX, y):
    numLen = len(str(number))
    startX = endX - numLen + 1

    arrOfNums.append({
        "num": number,
        "counted": False
    })

    arrIx = len(arrOfNums) - 1

    addXYVal(startX - 1, y, arrIx)
    addXYVal(endX + 1, y, arrIx)

    for i in range(startX - 1, endX + 2):
        addXYVal(i, y-1, arrIx)
        addXYVal(i, y+1, arrIx)

def addXYVal(x, y, index):
    if x not in iOfLocs:
        iOfLocs[x] = {}
    if y not in iOfLocs[x]:
        iOfLocs[x][y] = []
    iOfLocs[x][y].append(index)

lineNum = -1
while True:
    # Get each line and break if blank
    line = input.readline()
    if not line:
        break
    lineNum += 1

    runningNum = 0
    # Get first number
    for i in range(0, len(line)):
        if line[i].isnumeric():
            runningNum *= 10
            runningNum += int(line[i])
        elif runningNum == 0:
            runningNum = 0
        else:
            updateArrays(runningNum, i - 1, lineNum)
            runningNum = 0
        if line[i] == "*":
            iOfRandomChars.append({ "x": i, "y": lineNum })

# Done with setup, actually add everything now
for loc in iOfRandomChars:
    if loc["x"] not in iOfLocs or loc["y"] not in iOfLocs[loc["x"]]:
        continue
    arr = iOfLocs[loc["x"]][loc["y"]]
    print(arr)
    if len(arr) != 2:
        continue
    print("num1 " + str(arrOfNums[arr[0]]["num"]))
    print("num2 " + str(arrOfNums[arr[1]]["num"]))
    runningTotal += (arrOfNums[arr[0]]["num"] * arrOfNums[arr[1]]["num"])


print(runningTotal)
input.close()