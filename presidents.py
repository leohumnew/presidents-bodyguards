# --- PRESIDENTS PROBLEM: Boat not safe ---

coupleNum = 3
boatCapacity = 2
presidents = [coupleNum, 0, 0]
bodyguards = [coupleNum, 0, 0]
posMov = []
finalMoves = []

def createMoves():
    for i in range(boatCapacity+1):
        posMov.append([i, boatCapacity-i])
    for i in range(1, boatCapacity):
        posMov.append([i, 0])

def check(pres, bod):
    if pres[0] < 0 or pres[1] < 0 or bod[0] < 0 or bod[1] < 0 :
        return False
    if ((pres[0] != 0 and bod[0] != 0) and bod[0] < pres[0]) or ((pres[1] != 0 and bod[1] != 0) and bod[1] < pres[1]):
        return False
    return True

def tryMoves(pres, bod, movingRight, lastMove, currentMoves):
    # Check if valid state
    if not check(pres, bod):
        #print("INV: " + str(pres[0]) + " " + str(bod[0]) + " || " + str(pres[1]) + " " + str(bod[1]))
        # for m in currentMoves:
        #     print("HELP   " + str(m[0][0]) + " " + str(m[1][0]) + " || " + str(m[0][1]) + " " + str(m[1][1]))
        # print("------------------------")
        return False
    # Check end state
    if pres == [0, coupleNum] and bod == [0, coupleNum]:
        for m in currentMoves:
            print(str(m[0][0]) + "P " + str(m[1][0]) + "B || " + str(m[0][1]) + "P " + str(m[1][1]) + "B")
        print(str(pres[0]) + "P " + str(bod[0]) + "B || " + str(pres[1]) + "P " + str(bod[1]) + "B <- END")
        return True
    
    # Append current move to array storing sequence
    currentMoves.append([pres, bod])

    # Recursively call tryMoves function
    if movingRight:
        for j in range(len(posMov)):
            i = posMov[j]
            if lastMove != i and tryMoves([pres[0] - i[0], pres[1] + i[0]], [bod[0] - i[1], bod[1] + i[1]], not movingRight, i, currentMoves):
                return True
    else:
        for j in range(len(posMov)):
            i = posMov[j]
            if lastMove != i and tryMoves([pres[0] + i[0], pres[1] - i[0]], [bod[0] + i[1], bod[1] - i[1]], not movingRight, i, currentMoves):
                return True
    # No possible moves found
    return False


# START
createMoves()

if tryMoves(presidents, bodyguards, True, -1, []):
    print("Success!")
else:
    print("Could not find solution...")