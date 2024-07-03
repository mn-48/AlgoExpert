# O(w*h) Time | O(w*h) Space

def revealMinesweeper(board, row, column):
    if board[row][column] == "M":
        board[row][column] = "X"
        return board
    neighbors = getNeighbors(board, row, column)
    
    adjacentMinesCount = 0
    for neighborRow,  neighborColumn in neighbors: # O(8) this does not affect the solutions
        if board[neighborRow][neighborColumn] == "M":
            adjacentMinesCount += 1
    if adjacentMinesCount > 0:
        board[row][column] = str(adjacentMinesCount)
    else:
        board[row][column] = '0'
        for neighborRow,  neighborColumn in neighbors:
            if board[neighborRow][neighborColumn]=="H":
                revealMinesweeper(board,  neighborRow,  neighborColumn)
    

    return board


def getNeighbors(board, row, column):
    directions = [
        [-1, 1], [0, 1], [1, 1],
        [-1, 0], [1, 0],
        [-1, -1], [0, -1], [1, -1]
    ]

    neighbors = []
    for directionRow, directionColumn in directions:
        new_row = row + directionRow
        new_column = column + directionColumn
        
        if 0<= new_row < len(board) and 0<= new_column < len(board[0]):
            neighbors.append([new_row, new_column])
    return neighbors


if __name__ == "__main__":

    board = [
        ["H", "H", "H", "H", "M"],
        ["H", "1", "M", "H", "1"],
        ["H", "H", "H", "H", "H"],
        ["H", "H", "H", "H", "H"],
    ]
    row = 3
    column = 4
    expected = [
        ["0", "1", "H", "H", "M"],
        ["0", "1", "M", "2", "1"],
        ["0", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
    ]

    ans = revealMinesweeper(board, row, column)
    print(ans)
