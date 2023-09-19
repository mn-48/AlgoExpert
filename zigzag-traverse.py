# O(n) Time | O(n) Space

def zigzagTraverse(array):
    row, last_row = 0, len(array)-1
    col, last_col = 0, len(array[0])-1

    down = True
    output = []

    while row <= last_row and col <= last_col:
        output.append(array[row][col])

        if down:
            if row == last_row:
                down = False
                col +=1
            elif col==0:
                down = False
                row +=1
            else:
                row +=1
                col -=1
        else:
            if col == last_col:
                down = True
                row +=1
            elif row==0:
                down = True
                col+=1
            else:
                row -= 1
                col += 1
                
    return output


# array = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]
# output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# print(zigzagTraverse(array))