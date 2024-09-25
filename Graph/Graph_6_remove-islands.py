
# O(w*h) Time | O(w*h) Space

def removeIslands(matrix):
    height = len(matrix)
    width = len(matrix[0])
    
    # iterate border
    for i in range(height):
        for j in range(width):
            if (i>0  and i<height-1) and (j>0 and j< width-1):
                continue
            traverseIlands(matrix, i, j, True)
    
    # iterate inside
    for i in range(1, height):
        for j in range(1, width):
            traverseIlands(matrix, i, j, False)
    # 2 change back to 1
    for i in range( height):
        for j in range( width):
            if matrix[i][j]==2:
                matrix[i][j]=1
    
    
        
    return matrix

def traverseIlands(matrix, i, j, isBorder):
    if matrix[i][j] !=1:
        return
    if isBorder:
        matrix[i][j] = 2
    else:
        matrix[i][j] = 0
        
    if i>0:
        traverseIlands(matrix, i-1, j, isBorder)
        
    if j>0:
        traverseIlands(matrix, i, j-1, isBorder)
        
    if i<len(matrix)-1:
        traverseIlands(matrix, i+1, j, isBorder)
        
    if j<len(matrix[0])-1:
        traverseIlands(matrix, i, j+1, isBorder)
        
    
    


if __name__=="__main__":
    
    input = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    ans = removeIslands(input)
    print(ans)