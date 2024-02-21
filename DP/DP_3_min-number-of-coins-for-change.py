# O(nd) Time | O(n) Space

def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    numberOfCoins = [float('inf')]*(n+1)
    numberOfCoins[0] = 0
    for denom in denoms:
        for amount in range(1, n):
            if denom <= amount: 
                numberOfCoins[amount] = min(numberOfCoins[amount], 1+numberOfCoins[amount-denom])
    return numberOfCoins[n] if numberOfCoins[n] != float('inf') else -1