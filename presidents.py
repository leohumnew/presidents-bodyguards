# Coded by Leo Humphreys Newman w/ help from Nick Haynes
# --------- PRESIDENTS PROBLEM: Boat not safe ----------

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
bestDepth = [-1,-1] # Normal, symmetrical

# Create list of possible moves
def createMoves():
    for i in range(0, boatCapacity+2):
        for j in range(0, boatCapacity+2):
            if (i + j <= boatCapacity) and not (i == 0 and j == 0) and (i == 0 or j <= i):
                posMov.append([j, i])
    # print(posMov)

# Check if state is valid
def isValidState(pres, bod):
    if pres[0] < 0 or pres[1] < 0 or bod[0] < 0 or bod[1] < 0:
        return False
    if (pres[0] != 0 and bod[0] != 0 and bod[0] < pres[0]) or (pres[1] != 0 and bod[1] != 0 and bod[1] < pres[1]):
        return False
    return True

# Convert president + bodyguard count to couples + presidents + bodyguards
def toCouples(presCount, bodCount):
    if presCount == 0 or bodCount == 0:
        return (str(presCount) + "*P " if presCount != 0 else "") + (str(bodCount) + "*B " if bodCount != 0 else "")
    else:
        return (str(presCount) if presCount < bodCount else str(bodCount)) + "*C " + ((str(abs(presCount - bodCount)) + ("*P " if presCount - bodCount > 0 else "*B ")) if abs(presCount - bodCount) != 0 else "")

# Pretty-print sequence of moves
def printMoves(moves, states, symmetrical):
    # Init state
    print("{ " + toCouples(states[0][0][0], states[0][1][0]) + "|| " + toCouples(states[0][0][1], states[0][1][1]) + "}")
    # Before symmetry / moves when no symmetry
    for i in range(1, len(states)):
        if i%2 == 1: # Moving right
            print("\t" + toCouples(states[i][0][0], states[i][1][0]) + "| " + toCouples(moves[i][0], moves[i][1]) + "→ | " + toCouples(states[i][0][1]-moves[i][0], states[i][1][1]-moves[i][1]))
        else: # Moving left
            print("\t" + toCouples(states[i][0][0]-moves[i][0], states[i][1][0]-moves[i][1]) + "| ← " + toCouples(moves[i][0], moves[i][1]) + "| " + toCouples(states[i][0][1], states[i][1][1]))
        print("{ " + toCouples(states[i][0][0], states[i][1][0]) + "|| " + toCouples(states[i][0][1], states[i][1][1]) + "}")
    # If symmetry
    if symmetrical:
        for i in range(len(states)-3, -1, -1):
            if i%2 == 0: # Moving right
                print("\t" + toCouples(states[i][0][1], states[i][1][1]) + "| " + toCouples(moves[i+1][0], moves[i+1][1]) + "→ | " + toCouples(states[i][0][0]-moves[i+1][0], states[i][1][0]-moves[i+1][1]))
            else: # Moving left
                print("\t" + toCouples(states[i][0][1]-moves[i+1][0], states[i][1][1]-moves[i+1][1]) + "| ← " + toCouples(moves[i+1][0], moves[i+1][1]) + "| " + toCouples(states[i][0][0], states[i][1][0]))
            print("{ " + toCouples(states[i][0][1], states[i][1][1]) + "|| " + toCouples(states[i][0][0], states[i][1][0]) + "}")

# Recursive function to calculate valid sequence
def tryMoves(pres, bod, currentMoves, currentStates, moveRight, depth, lastMove):
    # Check if already been in this state to prevent getting stuck in loop
    if [pres, bod] in currentStates:
        return False
    
    # Check if valid state
    if not isValidState(pres, bod):
        return False

    global bestDepth
    # Check symmetrical end state
    if coupleNum%2 != 0 and ((moveRight and pres == [symNum+lastMove[0][0], symNum] and bod == [symNum+lastMove[0][1], symNum]) or (not moveRight and pres == [symNum, symNum+lastMove[0][0]] and bod == [symNum, symNum+lastMove[0][1]])):
        global bestAnswerSym
        if depth <= bestDepth[1] or bestDepth[1] == -1:
            # print("---- FOUND SYM ----")
            # printMoves(currentMoves+[lastMove[0]], currentStates+[[pres, bod]], True)
            bestDepth[1] = depth
            bestAnswerSym = [currentMoves+[lastMove[0]], currentStates+[[pres, bod]]]
        return False
    # Check non-symmetrical end state
    if pres == [0, coupleNum] and bod == [0, coupleNum]:
        global bestAnswer
        if depth <= bestDepth[0] or bestDepth[0] == -1:
            # print("-- FOUND NON-SYM --")
            # printMoves(currentMoves+[lastMove[0]], currentStates+[[pres, bod]], False)
            bestDepth[0] = depth
            bestAnswer = [currentMoves+[lastMove[0]], currentStates+[[pres, bod]]]
        return False

    # Recursively call tryMoves function
    if depth <= bestDepth[0] or bestDepth[0] == -1 or (coupleNum%2 != 0 and (depth <= bestDepth[1] or bestDepth[1] == -1)):
        for j in range(len(posMov)):
                i = posMov[j]
                if not (i == lastMove[0] and i == lastMove[1] ):
                    if moveRight:
                        if tryMoves([pres[0] - i[0], pres[1] + i[0]], [bod[0] - i[1], bod[1] + i[1]], currentMoves+[lastMove[0]], currentStates+[[pres, bod]], False, depth+1, [i, lastMove[0]]):
                            return True
                    else:
                        if tryMoves([pres[0] + i[0], pres[1] - i[0]], [bod[0] + i[1], bod[1] - i[1]], currentMoves+[lastMove[0]], currentStates+[[pres, bod]], True, depth+1, [i, lastMove[0]]):
                            return True
    return False


# START
createMoves()
tryMoves(presidents, bodyguards, [], [], True, 0, [[0,0],[0,0]])

if bestDepth[0] != -1:
    print("---- Best non-symmetrical answer ----\n")
    printMoves(bestAnswer[0], bestAnswer[1], False)
    print("")
if bestDepth[1] != -1:
    print("------ Best symmetrical answer ------\n")
    printMoves(bestAnswerSym[0], bestAnswerSym[1], True)
    print("")
if bestDepth == [-1, -1]:
    print("Could not find solution...")