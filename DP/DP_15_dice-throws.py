# # O(d*s*t) Time | O(t*s) Space
# def diceThrows(numDice, numSides, target):
#     storedResults = [[0] * (target+1) for _ in range(numDice+1)]    
#     storedResults[0][0] = 1
#     for currNumDicee in range(1, numDice+1):
#         for currTarget in range(target+1):
#             numWaysToReachTarget = 0
#             for currNumsides in range(1, min(currTarget, numSides)+1):
#                 numWaysToReachTarget += storedResults[currNumDicee-1][currTarget-currNumsides]
#             storedResults[currNumDicee][currTarget] = numWaysToReachTarget
            
#     return storedResults[numDice][target]


# O(d*s*t) Time | O(t) Space
def diceThrows(numDice, numSides, target):
    storedResults = [[0] * (target+1), [0] * (target+1),]    
    storedResults[0][0] = 1
    
    previousNumDiceIndex = 0
    newNumDiceIndex = 1
    for _ in range(numDice):
        for currTarget in range(target+1):
            numWaysToReachTarget = 0
            for currNumsides in range(1, min(currTarget, numSides)+1):
                numWaysToReachTarget += storedResults[previousNumDiceIndex][currTarget-currNumsides]
            storedResults[newNumDiceIndex][currTarget] = numWaysToReachTarget
        previousNumDiceIndex, newNumDiceIndex = newNumDiceIndex, previousNumDiceIndex
 
            
    return storedResults[previousNumDiceIndex][target]

if __name__=="__main__":
    numDice=3
    numSides=6 
    target=5
    res = diceThrows(numDice, numSides, target)
    print(res)
    