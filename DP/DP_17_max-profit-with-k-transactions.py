# # Time O(n^2*k) | Space (n*k)

# def maxProfitWithKTransactions(prices, k):
#     if not len(prices):
#         return 0
    
#     profits = [[0 for d in prices] for t in range(k+1)]
    
#     for t in range(1, k+1):
#         maxThusFar = float('-inf')
#         for d in range(1, len(prices)):
#             maxThusFar = max(maxThusFar, profits[t-1][d-1]-prices[d-1])
            
#             profits[t][d] = max(profits[t][d-1], maxThusFar+ prices[d])
#     print(profits)
    
#     return profits[-1][-1]



# Time O(n*k) | Space (n)

def maxProfitWithKTransactions(prices, k):
    if not len(prices):
        return 0
    
    oddProfits = [0 for d in prices] 
    evenProfits = [0 for d in prices] 
    
    for t in range(1, k+1):
        maxThusFar = float('-inf')
        for d in range(1, len(prices)):
            
            if t%2 ==1:
                currentProfits = oddProfits
                previousProfits = evenProfits
            else:
                currentProfits = evenProfits
                previousProfits = oddProfits
                
            maxThusFar = max(maxThusFar, previousProfits[d-1]-prices[d-1])
            
            currentProfits[d] = max(currentProfits[d-1], maxThusFar+ prices[d])
    # print(currentProfits)
    
    return evenProfits[-1] if k%2==0 else oddProfits[-1]


if __name__=="__main__":
    ans = maxProfitWithKTransactions([5, 11, 3, 50, 60, 90], 2)
    # 93
    print(ans)