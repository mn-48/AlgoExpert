# O(n*n*n) Time | O(1) Space
def squareOfZeroes(matrix):
    # Write your code here.
    n = len(matrix)

    def decodeValue(value):
        return [value//(n+1), value%(n+1)]
   
    def encodeValue(a,b):
        return a*(n+1)+b

    def prepareMatrix(): # O(n*n) Time | O(1) Space
        for x in range(n):
            # swap 0 <--> 1 in the matrix
            for y in range(n):
                inverse = 1- matrix[y][x]
                matrix[y][x] = encodeValue(inverse, inverse)
        # Store the number of zeros to the right and to the buttom in everry position
         
        for y in range(n-1, -1, -1):
            for x in range(n-1, -1, -1):
                prev_x = prev_y = 0
                if x!=n-1: prev_x = decodeValue(matrix[y][x+1])[0] # x not in the right edge
                if y!=n-1: prev_y = decodeValue(matrix[y+1][x])[1] # y not in the buttom edge

                a, b = decodeValue(matrix[y][x])
                if a>0: matrix[y][x] = encodeValue(a+prev_x, b)
                a, b = decodeValue(matrix[y][x])
                if b>0: matrix[y][x] = encodeValue(a, b+prev_y)
    prepareMatrix()

    for x1 in range(n): # O(n)
        for y1 in range(n): #O(n)
            max_size = min(decodeValue(matrix[y1][x1]))
            if max_size <= 1: continue

            for size in range(1, max_size): #O(n)
                x2 = x1+size
                y2 = y1+size

                if decodeValue(matrix[y2][x1])[0] < size+1: continue
                if decodeValue(matrix[y1][x2])[1] < size+1: continue
                return True

    return False
   