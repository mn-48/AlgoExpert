# O(n) time | O(1) space
#Time o(n) | Space O(N)
def spiralTraverse(array): 
    result = []
    start_row, end_row = 0, len(array)-1
    start_column, end_column = 0, len(array[0])-1


    while start_row <= end_row and start_column <= end_column:

        for col in range(start_column, end_column+1):
            result.append(array[start_row][col])

        for row in range(start_row+1, end_row+1):
            result.append(array[row][end_column])

        for col in reversed(range(start_column, end_column)):
            result.append(array[end_row][col])

        for row in reversed(range(start_row+1, end_row)):
            result.append(array[row][start_column])
        start_row+=1 
        end_row -=1 
        start_column+=1 
        end_column -=1
        
    return result
            

# =========================================================================
#Time o(n) | Space O(N)
def spiralTraverse(array):
    result = []
    while array:
        result += array.pop(0)
        array = list(zip(*array))[::-1]
    return result

# ======================================================================================
#Time o(n) | Space O(1)
def spiralTraverse(array):
    return array and [*array.pop(0)] + spiralTraverse([*zip(*array)][::-1])
    
# Time complexity O(n)
# Space complexity O(1)


'''
# Visualization

Here's how the matrix changes by always extracting the first row and rotating the remaining matrix counter-clockwise:

    |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
    |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
    |7 8 9|      |4 7|
Now look at the first rows we extracted:

    |1 2 3|      |6 9|      |8 7|      |4|      |5|
Those concatenated are the desired result.


# Another visualization
  spiral_order([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

= [1, 2, 3] + spiral_order([[6, 9],
                            [5, 8],
                            [4, 7]])

= [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
                                     [5, 4]])

= [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
                                              [5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

= [1, 2, 3, 6, 9, 8, 7, 4, 5]

'''
