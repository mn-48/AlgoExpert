# O(n) Time | O(1) Space
# def maximizeExpression(array):
#     # Write your code here.
#     if len(array) < 4:
#         return 0
#     a= b = c = d = float('-inf')
#     for x in array:
#         A = max(a, x)
#         B = max(b, a-x)
#         C = max(c, b+x)
#         D = max(d, c-x)
#         a, b, c, d = A, B, C, D
#     return d

def maximizeExpression(array):
    if len(array)<4:
        return 0
    maxOfA = [array[0]]
    maxOfAminusB = [float('-inf')]
    maxOfAminusBplusC = [float('-inf')]*2
    maxOfAminusBplusCminusD = [float('-inf')]*3
    
    for i in range(1, len(array)):
        currMax = max(maxOfA[i-1], array[i])
        maxOfA.append(currMax)
        
    for i in range(1, len(array)):
        currMax = max(maxOfAminusB[i-1], maxOfAminusB[i-1]-array[i])
        maxOfAminusB.append(currMax)
        
    for i in range(2, len(array)):
        currMax = max(maxOfAminusBplusC[i-1]+array[i], maxOfAminusBplusC[i-1])
        maxOfAminusBplusC.append(currMax)
        
    for i in range(3, len(array)):
        currMax = max(maxOfAminusBplusCminusD[i-1]-array[i], maxOfAminusBplusCminusD[i-1])
        maxOfAminusBplusCminusD.append(currMax)
        

    
    return maxOfAminusBplusCminusD[-1]
