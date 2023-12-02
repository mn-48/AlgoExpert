O(n^2) Time | O(n^2) Space
def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne)==0 and len(arrayTwo)==0:
        return True
    if arrayOne[0] != arrayTwo[0]:
        return False
    
    leftOne = getSmaller(arrayOne)
    leftTwo = getSmaller(arrayTwo)
    rightOne = getBiggerOrEgual(arrayOne)
    rightTwo = getBiggerOrEgual(arrayTwo)
    
    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)

def getSmaller(array):
    return [x for x in array[1:] if x < array[0]]

def getBiggerOrEgual(array):
    return [x for x in array[1:] if x >= array[0]]

# # ========================================================
# # O(n^2) Time | O(d) Space
# def sameBsts(arrayOne, arrayTwo):
#     return aresameBsts(arrayOne, arrayTwo, 0, 0, float('-inf'), float('inf'))
# def aresameBsts(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
#     if rootIdxOne == -1 or rootIdxTwo ==-1:
#         return rootIdxOne==rootIdxTwo
    
#     if arrayOne[rootIdxOne] !=  arrayTwo[rootIdxTwo]:
#         return False
    
#     leftRootIdxOne = getIndxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
#     leftRootIdxTwo = getIndxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)

#     rightRootIdxOne = getIndxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxVal)
#     rightRootIdxTwo = getIndxOfFirstBiggerOrEqual(arrayTwo, rootIdxTwo, maxVal)

#     currentValue = arrayOne[rootIdxOne]
#     leftAreSame = aresameBsts(arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentValue)
#     rightAreSame = aresameBsts(arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentValue, maxVal)

#     return leftAreSame and rightAreSame

# def getIndxOfFirstSmaller(array, startingIdx, minVal):
#     for i in range(startingIdx+1, len(array)):
#         if array[i] < array[startingIdx] and array[startingIdx] >= minVal:
#             return i
#     return -1

# def getIndxOfFirstBiggerOrEqual(array, startingIdx, maxVal):
#     for i in range(startingIdx+1, len(array)):
#         if array[i] > array[startingIdx] and array[startingIdx] < maxVal:
#             return i
#     return -1
    

