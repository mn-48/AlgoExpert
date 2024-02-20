# O(n) Time | O(n) Space

def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array)==1:
        return array[0]

    maxSums = array[:]

    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
         maxSums[i] = max(maxSums[i-1], maxSums[i-2]+array[i])
    return maxSums[-1]


# O(n) Time | O(1) Space
def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array)==1:
        return array[0]

    second = array[0]
    first = max(array[0], array[1])

    for i in range(2, len(array)):
        current = max(first, second+array[i])
        second = first
        first = current
    return first

# O(n) Time | O(1) Space
def maxSubsetSumNoAdjacent(array):
    currentMax, previousMax = 0, 0
    for i in range(len(array)):
        previousMax, currentMax = currentMax, max(currentMax, previousMax+array[i])
    return currentMax