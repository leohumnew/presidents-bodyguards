coupleNum = 3
#boatCapacity = input("Enter boat capacity: ")
presidents = [coupleNum, 0]
bodyguards = [coupleNum, 0]
posMov = [[2, 0], [0, 2], [1,1], [1,0]]
finalMoves = []

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
            print(str(m[0][0]) + " " + str(m[1][0]) + " || " + str(m[0][1]) + " " + str(m[1][1]))
        print(str(pres[0]) + " " + str(bod[0]) + " || " + str(pres[1]) + " " + str(bod[1]) + " <- END")
        return True
    
    #print(str(pres[0]) + " " + str(bod[0]) + " || " + str(pres[1]) + " " + str(bod[1]))
    currentMoves.append([pres, bod])

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
    return False

if tryMoves(presidents, bodyguards, True, -1, []):
    print("yay")
    
else:
    print("cry")