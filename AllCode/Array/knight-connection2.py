# # O(n*m) Time | O(n*m) Space

# import math
# def knightConnection(knightA, knightB):
#     # Write your code here.
#     possibleMoves = [
#         [-2, 1],
#         [-1, 2],
#         [1, 2],
#         [2, 1],
#         [2, -1],
#         [1, -2],
#         [-1, -2],
#         [-2, -1],
#     ]

#     queue = [[knightA[0], knightA[1], 0]]
#     visited = {positionToString(knightA)}
#     # print(visited)

#     while True:
#         currentPosition = queue.pop(0)
#         # print(currentPosition)

#         if currentPosition[0] == knightB[0] and currentPosition[1] == knightB[1]:
#             return math.ceil(currentPosition[2]/2)
        
#         for possibleMove in possibleMoves:
#             position = [currentPosition[0]+possibleMove[0], currentPosition[1]+possibleMove[1]]
#             positionString = positionToString(position)

#             if positionString not in visited:
#                 position.append(currentPosition[2]+1)
#                 queue.append(position)
#                 visited.add(positionString)



# def positionToString(position):
#     return ",".join(map(str, position))



# O(1) Time | O(1) Space
def knightConnection(knightA, knightB):
    dx, dy = abs(knightA[0] - knightB[0]), abs(knightA[1] - knightB[1])
    if dx < dy:
        dx, dy = dy, dx
    if dx * dy == 1:
        return 1
    if (dx, dy) in [(1, 0), (2, 2)]:
        return 2
    t = dy - dx // 2 - dx % 2 * 2
    return (1 + dx // 4 * 2 + dx % 4 + (t // 3 + t % 3 - dx // 2 % 2 if t >= 0 else (1 - dx // 2 % 2 * 2) * (dy % 2))) // 2

knightA = [0, 0]
knightB = [4, 2]
print(knightConnection(knightA, knightB))
