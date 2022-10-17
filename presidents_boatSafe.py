# --- PRESIDENTS PROBLEM: Boat safe ---

coupleNum = int(input("Enter number of couples: "))
print("")
boatCapacity = 2
presidents = [coupleNum, 0, 0]
bodyguards = [coupleNum, 0, 0]
posMov = []
posMovInit = [[2,0],[0,2],[1,1]]
finalMoves = []
stage = 0

# Create list of possible moves
def createMoves():
    # for i in range(boatCapacity+1):
    #     posMov.append([i, boatCapacity-i])
    # for i in range(1, boatCapacity):
    #     posMov.append([i, 0])
    return [[-1,-1], [-2,0], [0,-2], [1,0], [0,1], [-2,2], [-2,1], [-1,1], [-1,0], [2,-2], [1,-2], [1,-1], [0,-1], [-1,0], [0,-1], [-1,1], [1,-1]]

# Check if state is valid
def check(pres, bod):
    if pres[0] < 0 or pres[1] < 0 or pres[2] < 0 or bod[0] < 0 or bod[1] < 0 or bod[2] < 0 or pres[1] + bod[1] > boatCapacity or pres[1] + bod[1] < 1:
        return False
    if (pres[0] != 0 and bod[0] != 0 and bod[0] < pres[0]) or (pres[2] != 0 and bod[2] != 0 and bod[2] < pres[2]):
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
    print(str(moves[len(moves)-1][0][0]) + " " + str(moves[len(moves)-1][1][0]) + " |     " + str(moves[len(moves)-1][0][1]) + " " + str(moves[len(moves)-1][1][1]) + "     | " + str(moves[len(moves)-1][0][2]) + " " + str(moves[len(moves)-1][1][2]) + "   END")

# Recursive function to calculate valid sequence
def tryMoves(pres, bod, currentMoves, stage, init):
    if [pres, bod] in currentMoves:
        return False

    # Append current move to array storing sequence
    currentMoves = currentMoves + [[pres, bod]]

    # Check end state
    if pres == [0, 0, coupleNum] and bod == [0, 0, coupleNum]:
        printMoves(currentMoves)
        return True
    # Check if valid state
    if not init == 1 and not check(pres, bod):
        #printMoves(currentMoves)
        #print("----- FAILURE -----")
        return False

    # Recursively call tryMoves function
    if init == 0:
        for j in range(len(posMov)):
                i = posMov[j]
                # Stage 0 is left bank interchange, stage 1 is right bank interchange
                if stage == 0:
                    if tryMoves([pres[0] - i[0], pres[1] + i[0], pres[2]], [bod[0] - i[1], bod[1] + i[1], bod[2]], currentMoves, 1, 0):
                        return True
                elif stage == 1:
                    if tryMoves([pres[0], pres[1] + i[0], pres[2] - i[0]], [bod[0], bod[1] + i[1], bod[2] - i[1]], currentMoves, 0, 0):
                        return True
    else:
        for j in range(len(posMovInit)):
                i = posMovInit[j]
                if tryMoves([pres[0] - i[0], pres[1] + i[0], pres[2]], [bod[0] - i[1], bod[1] + i[1], bod[2]], currentMoves, 1, 0):
                    return True

    currentMoves = currentMoves[:-1] 
    return False


# START
posMov = createMoves()
if tryMoves(presidents, bodyguards, [], 0, 1):
    print("\n------- Success! -------\n")
else:
    print("Could not find solution...")