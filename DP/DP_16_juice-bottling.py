# O(n^3) Time | O(n^2) Space

def juiceBottling(prices):
    numSizes = len(prices)
    maxProfit = [0] * numSizes
    solusions = [[]] * numSizes
    
    for size in range(numSizes):
        for dividingPoint in range(size+1):
            possibleProfit = maxProfit[size -dividingPoint] + prices[dividingPoint]
            
            if possibleProfit > maxProfit[size]:
                maxProfit[size] = possibleProfit
                solusions[size] = [dividingPoint] + solusions[size-dividingPoint]
                
    return solusions[-1]

# # ===========================================================
# # O(n^2) Time | O(n) Space

# def juiceBottling(prices):
#     numSizes = len(prices)
#     maxProfit = [0] * numSizes
#     dividingPoints = [0] * numSizes
    
#     for size in range(numSizes):
#         for dividingPoint in range(size+1):
#             possibleProfit = maxProfit[size -dividingPoint] + prices[dividingPoint]
            
#             if possibleProfit > maxProfit[size]:
#                 maxProfit[size] = possibleProfit
#                 dividingPoints[size] = dividingPoint
                
#     solusion = []
#     currentDividingPoint = numSizes -1
#     while currentDividingPoint > 0:
#         solusion.append(dividingPoints[currentDividingPoint])
#         currentDividingPoint -= dividingPoints[currentDividingPoint]
#     return solusion
