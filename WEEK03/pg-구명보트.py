import sys
def solution(people, limit):
    global wPeople, wLimit, boatCnt, weightSum
    wPeople=sorted(people)
    wLimit=limit
    
    boatCnt = 0
    
    saveByBoat()

    return boatCnt


def saveByBoat():
    global wPeople, wLimit, boatCnt, weightSum
    idx = 0
    boat = []
    for i in reversed(range(len(wPeople))):
        if i in boat: continue
        boatCnt +=1
        weightSum = 0 
        boat += [i]
        weightSum += wPeople[i]
        if not idx in boat:
            for j in range(idx, i):
                if wPeople[j]+weightSum <= wLimit:
                    boat += [j]
                    weightSum += wPeople[j]
                else: 
                    idx=j
                    break 
