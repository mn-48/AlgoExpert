# Time O(w*h) | Space O(w*h)

def transposeMatrix(matrix):
    transposedMatrix = []

    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        transposedMatrix.append(newRow)
    return transposedMatrix
    
    
# def transposeMatrix(matrix):
#     return list(zip(*matrix))


if __name__=="__main__":
    input = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ans = transposeMatrix(input)
    print(ans)