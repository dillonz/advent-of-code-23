input = open("input.txt", "r")
runningTotal = 0

while True:
    # Get each line and break if blank
    line = input.readline()
    if not line:
        break
    # Loop through each character and reset running variables
    mostRecentNum = 0
    foundFirst = False
    for char in line:
        # If it's a number, store it in most recent num and put it in
        # the tens place if this is the first number
        if char.isnumeric():
            mostRecentNum = int(char)
            if not foundFirst:
                foundFirst = True
                runningTotal += 10 * mostRecentNum
    # Add the last number to the running total (the ones place)
    runningTotal += mostRecentNum

print(runningTotal)
input.close()