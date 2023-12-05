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
    for index in range(0, len(line)):
        char = line[index]
        # If it's a number, store it in most recent num
        if char.isnumeric():
            mostRecentNum = int(char)
        elif char in ['o', 't', 'f', 's', 'e', 'n']:
            print(type(index))
            if (char == 'o') and (len(line) >= index + 3) and (line[index:index+3] == "one"):
                mostRecentNum = 1
            elif (char == 't') and (len(line) >= index + 3) and (line[index:index+3] == "two"):
                mostRecentNum = 2
            elif (char == 't') and (len(line) >= index + 5) and (line[index:index+5] == "three"):
                mostRecentNum = 3
            elif (char == 'f') and (len(line) >= index + 4) and (line[index:index+4] == "four"):
                mostRecentNum = 4
            elif (char == 'f') and (len(line) >= index + 4) and (line[index:index+4] == "five"):
                mostRecentNum = 5
            elif (char == 's') and (len(line) >= index + 3) and (line[index:index+3] == "six"):
                mostRecentNum = 6
            elif (char == 's') and (len(line) >= index + 5) and (line[index:index+5] == "seven"):
                mostRecentNum = 7
            elif (char == 'e') and (len(line) >= index + 5) and (line[index:index+5] == "eight"):
                mostRecentNum = 8
            elif (char == 'n') and (len(line) >= index + 4) and (line[index:index+4] == "nine"):
                mostRecentNum = 9
        # If this is the first number we found, set that we found it first and add it in the
        # tens place
        if (not foundFirst) and (mostRecentNum > 0):
            foundFirst = True
            runningTotal += 10 * mostRecentNum

                    

    # Add the last number to the running total (the ones place)
    runningTotal += mostRecentNum

print(runningTotal)
input.close()