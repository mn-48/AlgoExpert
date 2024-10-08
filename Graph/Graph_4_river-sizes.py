# O(w*h) Time | O(w*h) Space

def riverSizes(matrix):
    sizes = []
    visited = [[False for col in row] for row in matrix]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)

    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodeToExplore = [[i, j]]
    
    while len(nodeToExplore):
        currentNode = nodeToExplore.pop()
        
        i = currentNode[0]
        j = currentNode[1]
        
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j]==0:
            continue
        
        currentRiverSize +=1
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        
        for neighbor in unvisitedNeighbors:
            nodeToExplore.append(neighbor)
            
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)
    

def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    
    if i>0 and not visited[i-1][j]:
        unvisitedNeighbors.append([i-1, j])
        
    if i<len(matrix)-1 and not visited[i+1][j]:
        unvisitedNeighbors.append([i+1, j])
    
    if j>0 and not visited[i][j-1]:
        unvisitedNeighbors.append([i, j-1])
        
    if j<len(matrix[0])-1 and not visited[i][j+1]:
        unvisitedNeighbors.append([i, j+1])
    return unvisitedNeighbors
    



if __name__ == "__main__":

    testInput = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]


    ans = riverSizes(testInput)
    print(ans)