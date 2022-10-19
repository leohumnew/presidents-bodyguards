# --- PRESIDENTS PROBLEM: Boat not safe ---

# Inputs
from re import T


coupleNum = int(input("Enter number of couples: "))
symNum = (coupleNum - 1) / 2
boatCapacity = int(input("Enter boat capacity: "))
print("")
# State arrays
presidents = [coupleNum, 0]
bodyguards = [coupleNum, 0]
# Posible moves
posMov = []
# Answer variables
bestAnswer = []
bestAnswerSym = []
bestDepth = -1
bestDepthSym = -1
foundAnswer = 0
# Stage (0 = left exchange, 1 = right exchange)
stage = 0

# Create list of possible moves
def createMoves():
    for i in range(0, boatCapacity+1):
        for j in range(0, boatCapacity+1):
            if (i + j < boatCapacity) and not (i == 0 and j == 0):
                posMov.append([i, j])

# Check if state is valid
def isValidState(pres, bod):
    if pres[0] < 0 or pres[1] < 0 or bod[0] < 0 or bod[1] < 0:
        return False
    if (pres[0] != 0 and bod[0] != 0 and bod[0] < pres[0]) or (pres[1] != 0 and bod[1] != 0 and bod[1] < pres[1]):
        return False
    return True

# Pretty-print one move
# def printMove(move):


# Pretty-print sequence of moves
def printMoves(moves):
    print("{ " + str(moves[0][0][0]) + "p " + str(moves[0][1][0]) + "b || " + str(moves[0][0][1]) + "p " + str(moves[0][1][1]) + "b }\t\tSTART")
    for i in range(1, len(moves)):
        if i%2:
            print("\t" + str(moves[i][0][0]) + "p " + str(moves[i][1][0]) + "b | " + str(moves[i][2][0]) + "p " + str(moves[i][2][1]) + "b | " + str(moves[i][0][1]-moves[i][2][0]) + "p " + str(moves[i][1][1]-moves[i][2][1]) + "b")
        else:
            print("\t" + str(moves[i][0][0]-moves[i][2][0]) + "p " + str(moves[i][1][0]-moves[i][2][0]) + "b | " + str(moves[i][2][0]) + "p " + str(moves[i][2][1]) + "b | " + str(moves[i][0][1]) + "p " + str(moves[i][1][1]) + "b")
        print("{ " + str(moves[i][0][0]) + "p " + str(moves[i][1][0]) + "b || " + str(moves[i][0][1]) + "p " + str(moves[i][1][1]) + "b }")
    if foundAnswer == 1:
        print(str(moves[-1][0][0]) + "p " + str(moves[-1][1][0]) + "b |     " + str(moves[-1][0][1]) + "p " + str(moves[-1][1][1]) + "b     | " + str(moves[-1][0][2]) + "p " + str(moves[-1][1][2]) + "b   END")
    else:
        for i in range(len(moves)-2, 0, -1):
            if i%2:
                print("\t" + str(moves[i][0][1]) + "p " + str(moves[i][1][1]) + "b | " + str(moves[i][2][0]) + "p " + str(moves[i][2][1]) + "b | " + str(moves[i][0][0]-moves[i+1][2][0]) + "p " + str(moves[i][1][0]-moves[i+1][2][1]) + "b")
            else:
                print("\t" + str(moves[i][0][1]-moves[i+1][2][0]) + "p " + str(moves[i][1][1]-moves[i+1][2][0]) + "b | " + str(moves[i][2][0]) + "p " + str(moves[i][2][1]) + "b | " + str(moves[i][0][0]) + "p " + str(moves[i][1][0]) + "b")
            print("{ " + str(moves[i][1][1]) + "p " + str(moves[i][1][1]) + "b || " + str(moves[i][0][0]) + "p " + str(moves[i][1][0]) + "b }")
        
        #print(str(moves[0][0][2]) + "p " + str(moves[0][1][2]) + "b |    " + str(moves[0][0][1]) + "p " + str(moves[0][1][1]) + "b    | " + str(moves[0][0][0]) + "p " + str(moves[0][1][0]) + "b   END")

# Recursive function to calculate valid sequence
def tryMoves(pres, bod, currentMoves, moveRight, depth, lastMove):
    if [pres, bod] in currentMoves:
        return False

    # Append current move to array storing sequence
    currentMoves = currentMoves + [[pres, bod, lastMove]]

    global bestDepth
    # Check end state
    if (pres == [0, coupleNum] and bod == [0, coupleNum]) or (moveRight and pres == [symNum-lastMove[0], symNum] and bod == [symNum-lastMove[1], symNum]) or (not moveRight and pres == [symNum, symNum-lastMove[0]] and bod == [symNum, symNum-lastMove[1]]):
        global bestAnswer, foundAnswer
        if (len(currentMoves) < len(bestAnswer)) or not foundAnswer:
            # print("--- CURRENT BEST ---")
            # printMoves(currentMoves)
            bestDepth = depth
            bestAnswer = currentMoves
            if (pres == [0, coupleNum] and bod == [0, coupleNum]):
                foundAnswer = 1
            else:
                foundAnswer = 2
        return False
    
    # Check if valid state
    if not isValidState(pres, bod):
        printMoves(currentMoves)
        print("----- FAILURE -----")
        return False

    # Recursively call tryMoves function
    if depth < bestDepth or bestDepth == -1:
        for j in range(len(posMov)):
                i = posMov[j]
                if moveRight:
                    if tryMoves([pres[0] - i[0], pres[1] + i[0]], [bod[0] - i[1], bod[1] + i[1]], currentMoves, False, depth+1, i):
                        return True
                else:
                    if tryMoves([pres[0] + i[0], pres[1] - i[0]], [bod[0] + i[1], bod[1] - i[1]], currentMoves, True, depth+1, i):
                        return True

    currentMoves = currentMoves[:-1] 
    return False


# START
createMoves()

tryMoves(presidents, bodyguards, [], True, 0, [0,0])
if foundAnswer:
    print("---------- Success! ----------\n")
    printMoves(bestAnswer)
    print("")
else:
    print("Could not find solution...")