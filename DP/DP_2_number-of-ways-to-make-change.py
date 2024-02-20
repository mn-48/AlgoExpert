# O(nd) Time | O(n) Space

def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    ways = [1]+[0]*n

    for i in denoms:
        for j in range(i, len(ways)):
            ways[j] += ways[j-i]
    return ways[n]

