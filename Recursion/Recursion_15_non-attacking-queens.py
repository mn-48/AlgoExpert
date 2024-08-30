# O(n!) Time | O(n) Space


def nonAttackingQueens(n):
    count = 0
    posDiag = set()
    negDiag = set()
    cols = set()
    
    def dfs(row):
        nonlocal count
        
        if row >= n:
            count +=1
        
        for col in range(n):
            if col in cols or (row+col) in posDiag or (row-col) in negDiag:
                continue
            cols.add(col)
            posDiag.add(row+col)
            negDiag.add(row-col)
            
            dfs(row+1)
            cols.remove(col)
            posDiag.remove(row+col)
            negDiag.remove(row-col)
            
    dfs(0)
    return count

if __name__=="__main__":
    input = 4
    expected = 2
    ans = nonAttackingQueens(input)
    print(ans)