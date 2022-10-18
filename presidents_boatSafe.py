# --- PRESIDENTS PROBLEM: Boat safe ---

# Inputs
coupleNum = int(input("Enter number of couples: "))
symNum = (coupleNum - 1) / 2
boatCapacity = int(input("Enter boat capacity: "))
print("")
# State arrays
presidents = [coupleNum, 0, 0]
bodyguards = [coupleNum, 0, 0]
# Posible moves
posMov = []
posMovInit = []
# Answer variables
bestAnswer = []
bestAnswerSym = []
bestDepth = -1
bestDepthSym = -1
foundAnswer = False
# Stage (0 = left exchange, 1 = right exchange)
stage = 0

# Create list of possible moves
def createMoves():
    for i in range(-boatCapacity, boatCapacity+1):
        for j in range(-boatCapacity, boatCapacity+1):
            if (abs(i + j) < boatCapacity or i+j == -2) and not (i == 0 and j == 0):
                posMov.append([i, j])
    for i in range(boatCapacity+1):
        posMovInit.append([i, boatCapacity-i])

# Check if state is valid
def check(pres, bod):
    if pres[0] < 0 or pres[1] < 0 or pres[2] < 0 or bod[0] < 0 or bod[1] < 0 or bod[2] < 0 or pres[1] + bod[1] > boatCapacity or pres[1] + bod[1] < 1:
        return False
    if (pres[0] != 0 and bod[0] != 0 and bod[0] < pres[0]) or (pres[1] != 0 and bod[1] != 0 and bod[1] < pres[1]) or (pres[2] != 0 and bod[2] != 0 and bod[2] < pres[2]):
        return False
    return True

# Pretty-print sequence of moves
def printMoves(moves):
    print(str(moves[0][0][0]) + " " + str(moves[0][1][0]) + " |     " + str(moves[0][0][1]) + " " + str(moves[0][1][1]) + "     | " + str(moves[0][0][2]) + " " + str(moves[0][1][2]) + "   START")
    for i in range(1, len(moves)-1):
        if i%2 == 0:
            print(str(moves[i][0][0]) + " " + str(moves[i][1][0]) + " |  <- " + str(moves[i][0][1]) + " " + str(moves[i][1][1]) + "     | " + str(moves[i][0][2]) + " " + str(moves[i][1][2]))
        else:
            print(str(moves[i][0][0]) + " " + str(moves[i][1][0]) + " |     " + str(moves[i][0][1]) + " " + str(moves[i][1][1]) + " ->  | " + str(moves[i][0][2]) + " " + str(moves[i][1][2]))
    if moves[-1][0][1] == 0 and moves[-1][1][1] == 0:
        print(str(moves[-1][0][0]) + " " + str(moves[-1][1][0]) + " |     " + str(moves[-1][0][1]) + " " + str(moves[-1][1][1]) + "     | " + str(moves[-1][0][2]) + " " + str(moves[-1][1][2]) + "   END")
    else:
        print(str(moves[-1][0][0]) + " " + str(moves[-1][1][0]) + " |     " + str(moves[-1][0][1]) + " " + str(moves[-1][1][1]) + " ->  | " + str(moves[-1][0][2]) + " " + str(moves[-1][1][2]) + "   SYM")
        for i in range(len(moves)-2, 0, -1):
            if i%2 == 0:
                print(str(moves[i][0][2]) + " " + str(moves[i][1][2]) + " |  <- " + str(moves[i][0][1]) + " " + str(moves[i][1][1]) + "     | " + str(moves[i][0][0]) + " " + str(moves[i][1][0]))
            else:
                print(str(moves[i][0][2]) + " " + str(moves[i][1][2]) + " |     " + str(moves[i][0][1]) + " " + str(moves[i][1][1]) + " ->  | " + str(moves[i][0][0]) + " " + str(moves[i][1][0]))
        print(str(moves[0][0][2]) + " " + str(moves[0][1][2]) + " |     " + str(moves[0][0][1]) + " " + str(moves[0][1][1]) + "     | " + str(moves[0][0][0]) + " " + str(moves[0][1][0]) + "   END")

# Recursive function to calculate valid sequence
def tryMoves(pres, bod, currentMoves, stage, init, depth):
    if [pres, bod] in currentMoves:
        return False

    # Append current move to array storing sequence
    currentMoves = currentMoves + [[pres, bod]]

    global bestDepth
    # Check end state
    if (pres == [0, 0, coupleNum] and bod == [0, 0, coupleNum]) or (pres == [symNum, 1, symNum] and bod == [symNum, 1, symNum]):
        global bestAnswer, foundAnswer
        if (pres[0] == 0 and len(currentMoves) < len(bestAnswer)) or (len(currentMoves) < len(bestAnswer)) or not foundAnswer:
            # print("--- CURRENT BEST ---")
            # printMoves(currentMoves)
            bestDepth = depth
            bestAnswer = currentMoves
        foundAnswer = True
        return False
    
    # Check if valid state
    if not init == 1 and not check(pres, bod):
        #printMoves(currentMoves)
        #print("----- FAILURE -----")
        return False

    # Recursively call tryMoves function
    if init == 0 and (depth < bestDepth or bestDepth == -1):
        for j in range(len(posMov)):
                i = posMov[j]
                # Stage 0 is left bank interchange, stage 1 is right bank interchange
                if stage == 0:
                    if tryMoves([pres[0] - i[0], pres[1] + i[0], pres[2]], [bod[0] - i[1], bod[1] + i[1], bod[2]], currentMoves, 1, 0, depth + 1):
                        return True
                elif stage == 1:
                    if tryMoves([pres[0], pres[1] + i[0], pres[2] - i[0]], [bod[0], bod[1] + i[1], bod[2] - i[1]], currentMoves, 0, 0, depth + 1):
                        return True
    else:
        for j in range(len(posMovInit)):
                i = posMovInit[j]
                if tryMoves([pres[0] - i[0], pres[1] + i[0], pres[2]], [bod[0] - i[1], bod[1] + i[1], bod[2]], currentMoves, 1, 0, depth + 1):
                    return True

    currentMoves = currentMoves[:-1] 
    return False


# START
createMoves()

tryMoves(presidents, bodyguards, [], 0, 1, 0)
if foundAnswer:
    print("------- Success! -------\n")
    printMoves(bestAnswer)
    print("")
else:
    print("Could not find solution...")