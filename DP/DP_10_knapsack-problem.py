
# O(n*c) Time | )(n*c) Space

def knapsackProblem(items, capacity):
    knapsakValues = [[0 for x in range(capacity+1)] for y in range(len(items)+1)]
    for i in range(1, len(items)+1):
        currentValue = items[i-1][0]
        currentWeight = items[i-1][1]
        for c in range(capacity+1):
            if currentWeight > c:
                knapsakValues[i][c] = knapsakValues[i-1][c]
            else:
                knapsakValues[i][c] = max(knapsakValues[i-1][c], knapsakValues[i-1][c-currentWeight]+currentValue)

    # print(knapsakValues)
    return [knapsakValues[-1][-1], getKnapsakItems(knapsakValues, items)]

def getKnapsakItems(knapsakValues, items):
    i = len(knapsakValues)-1
    c = len(knapsakValues[0])-1

    sequence = []

    while i>0:
        if knapsakValues[i-1][c]==knapsakValues[i][c]:
            i-=1
        else:
            sequence.append(i-1)
            c -= items[i-1][1]
            i-=1
        if c==0:
            break
    return list(reversed(sequence))

    
        
if __name__=="__main__":
    items = [
        [1, 2],
        [4, 3],
        [5, 6],
        [6, 7]
    ]
    capacity = 10

    ans = knapsackProblem(items, capacity)
    print(ans)