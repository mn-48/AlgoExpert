# O(w*h) Time | O(w*h) Space

def revealMinesweeper(board, row, column):
    # Write your code here.
    return []


if __name__=="__main__":
    
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