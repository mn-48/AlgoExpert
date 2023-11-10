# O(n*m) Time | O(n*m) Space

import math
def knightConnection(knightA, knightB):
    # Write your code here.
    possibleMoves = [
        [-2, 1],
        [-1, 2],
        [1, 2],
        [2, 1],
        [2, -1],
        [1, -2],
        [-1, -2],
        [-2, -1],
    ]

    queue = [[knightA[0], knightA[1], 0]]
    visited = {positionToString(knightA)}
    # print(visited)

    while True:
        currentPosition = queue.pop(0)
        # print(currentPosition)

        if currentPosition[0] == knightB[0] and currentPosition[1] == knightB[1]:
            return math.ceil(currentPosition[2]/2)
        
        for possibleMove in possibleMoves:
            position = [currentPosition[0]+possibleMove[0], currentPosition[1]+possibleMove[1]]
            positionString = positionToString(position)

            if positionString not in visited:
                position.append(currentPosition[2]+1)
                queue.append(position)
                visited.add(positionString)



def positionToString(position):
    return ",".join(map(str, position))


