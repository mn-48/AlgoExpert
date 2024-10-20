# # O(w^2 * h^2) Time | O(w*h) Space

# def largestIsland(matrix):
#     maxSize = 0
#     for row in range(len(matrix)):
#         for col in range(len(matrix[0])):
#             if matrix[row][col] ==0:
#                 continue
#             maxSize = max(maxSize, getSizeFromNode(row, col, matrix))
#     return maxSize

# def getSizeFromNode(row, col, matrix):
#     size = 1

#     visited = [[False for value in row] for row in matrix]

#     nodeToExplore = getLandNeighbors(row, col, matrix)

#     while len(nodeToExplore):
#         currentNode = nodeToExplore.pop()
#         currentRow, currentCol = currentNode[0], currentNode[1]
#         if visited[currentRow][currentCol]:
#             continue
#         visited[currentRow][currentCol] = True
#         size +=1
#         nodeToExplore += getLandNeighbors(currentRow, currentCol, matrix)
#     return size


# def getLandNeighbors(row, col, matrix):
#     landNeighbors = []

#     if row > 0 and matrix[row-1][col] != 1:
#         landNeighbors.append([row-1, col])

#     if row < len(matrix)-1 and matrix[row+1][col] != 1:
#         landNeighbors.append([row+1, col])

#     if col > 0 and matrix[row][col-1] != 1:
#         landNeighbors.append([row, col-1])

#     if col < len(matrix[row])-1 and matrix[row][col+1] != 1:
#         landNeighbors.append([row, col+1])
    
#     return landNeighbors



# if __name__=="__main__":


#     matrix = [[0, 1, 1], [0, 0, 1], [1, 1, 0]]
#     ans = largestIsland(matrix)
#     print(ans)


    
# O(w* h) Time | O(w*h) Space

def largestIsland(matrix):
    islandSizes = []
    islandNUmber = 2
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] ==0:
                islandSizes.append(getSizeFromNode(row, col, matrix, islandNUmber))
                islandNUmber += 1 
    maxSize = 0 
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] !=1:
                continue

            landNeighbors = getLandNeighbors(row, col, matrix)
            islands = set()

            for neighbor in landNeighbors:
                islands.add(matrix[neighbor[0]] [neighbor[1]])
            size = 1
            for island in islands:
                size += islandSizes[island-2]
            maxSize = max(size, maxSize)


    return maxSize

def getSizeFromNode(row, col, matrix, islandNUmber):
    size = 0

    nodeToExplore = [[row, col]]

    while len(nodeToExplore):
        currentNode = nodeToExplore.pop()
        currentRow, currentCol = currentNode[0], currentNode[1]
        if matrix[currentRow][currentCol] !=0 :
            continue

        matrix[currentRow][currentCol] = islandNUmber
        size +=1
        nodeToExplore += getLandNeighbors(currentRow, currentCol, matrix)
    return size


def getLandNeighbors(row, col, matrix):
    landNeighbors = []

    if row > 0 and matrix[row-1][col] != 1:
        landNeighbors.append([row-1, col])

    if row < len(matrix)-1 and matrix[row+1][col] != 1:
        landNeighbors.append([row+1, col])

    if col > 0 and matrix[row][col-1] != 1:
        landNeighbors.append([row, col-1])

    if col < len(matrix[row])-1 and matrix[row][col+1] != 1:
        landNeighbors.append([row, col+1])
    
    return landNeighbors



if __name__=="__main__":


    matrix = [[0, 1, 1], [0, 0, 1], [1, 1, 0]]
    ans = largestIsland(matrix)
    print(ans)


    
