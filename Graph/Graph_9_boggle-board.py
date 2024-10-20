# O(nm*8^s+ws) Time | O(ws) Space 
def boggleBoard(board, words):
    # Write your code here.
    trie = Trie()
    for word in words:
        trie.add(word)
        
    finalWords = {}
    visited = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())

def explore(i, j, board, trieNode, visited, finalWords):
    if (i, j) in visited:
        return
    letter = board[i][j]
    if letter not in trieNode:
        return
    visited.add((i, j))
    trieNode = trieNode[letter]
    if "*" in trieNode:
        finalWords[trieNode["*"]] = True
    neighbors = getNeighbor(i, j, board)
    for neighbor in neighbors:
        explore(neighbor[0], neighbor[1], board, trieNode, visited, finalWords)
    visited.remove((i, j))

def getNeighbor(i, j, board):
    neighbors = []

    if i>0 and j>0:
        neighbors.append([i-1, j-1])
    if i>0 and j<len(board[0])-1:
        neighbors.append([i-1, j+1])
    if i < len(board)-1 and j < len(board[0])-1:
        neighbors.append([i+1, j+1])
    if i < len(board) -1 and j>0:
        neighbors.append([i+1, j-1])
    if i>0:
        neighbors.append([i-1, j])
    if i < len(board) - 1:
        neighbors.append([i+1, j])
    if j > 0:
        neighbors.append([i, j-1])
    if j < len(board[0])-1:
        neighbors.append([i, j+1])
    return neighbors



class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"
    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}

            current = current[letter]
        current[self.endSymbol] = word
            
if __name__=="__main__":

    board = [
        ["t", "h", "i", "s", "i", "s", "a"],
        ["s", "i", "m", "p", "l", "e", "x"],
        ["b", "x", "x", "x", "x", "e", "b"],
        ["x", "o", "g", "g", "l", "x", "o"],
        ["x", "x", "x", "D", "T", "r", "a"],
        ["R", "E", "P", "E", "A", "d", "x"],
        ["x", "x", "x", "x", "x", "x", "x"],
        ["N", "O", "T", "R", "E", "-", "P"],
        ["x", "x", "D", "E", "T", "A", "E"],
    ]
    words = [
        "this",
        "is",
        "not",
        "a",
        "simple",
        "boggle",
        "board",
        "test",
        "REPEATED",
        "NOTRE-PEATED",
    ]
    ans = boggleBoard(board, words)
    print(ans)