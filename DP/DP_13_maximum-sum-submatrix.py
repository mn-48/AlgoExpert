# O(w*h) Time | O(w*h) Space
def maximumSumSubmatrix(matrix, size):
    row = len(matrix)
    col = len(matrix[0])
    
    sums = createMatrix(matrix, row, col)
    # print(sums)
    maxSubMatrixSum = float('-inf')
    for i in range(size-1, row):
        for j in range(size-1, col):
            total = sums[i][j]
            
            touchTopBorder = i-size < 0
            touchLeftBorder = j-size < 0
            touchTopOrLeftBorder = touchTopBorder or touchLeftBorder
            if not touchTopBorder:
                total -= sums[i-size][j]
            
            if not touchLeftBorder:
                total -= sums[i][j-size]
            
            if not touchTopOrLeftBorder:
                total += sums[i-size][j-size]
            
            
            maxSubMatrixSum = max(maxSubMatrixSum, total)
    return maxSubMatrixSum

def createMatrix(matrix, row, col):
    # row = len(matrix)
    # col = len(matrix[0])
    sums = [[0] * col for r in range(row)]
    sums[0][0] = matrix[0][0]
    for i in range(1, col):
        sums[0][i] = sums[0][i-1] + matrix[0][i] 
        
    for i in range(1, row):
        sums[i][0] = sums[i-1][0]+ matrix[i][0]
        
    for i in range(1, row):
        for j in range(1, col):
            sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + matrix[i][j]
    
    return sums
    
    

    
    
    
if __name__=="__main__":
    matrix = [[5, 3, -1, 5], [-7, 3, 7, 4], [12, 8, 0, 0], [1, -8, -8, 2]]
    size = 2
    
    res = maximumSumSubmatrix(matrix, size)
    print(res)
