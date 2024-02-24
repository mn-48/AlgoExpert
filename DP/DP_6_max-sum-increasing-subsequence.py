# O(n^2) Time | O(n) Space
def maxSumIncreasingSubsequence(array):
    sequences  = [None] * len(array)
    # sequences  = [None for x in array] 
    sums = array[:]
    maxSumIdx = 0
    for i in range(len(array)):
        currentNumber = array[i]
        
        for j in range(0, i):
            otherNumber = array[j]
            
            if otherNumber < currentNumber and sums[j] + currentNumber >= sums[i]:
                sums[i] = sums[j] + currentNumber
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]


def  buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))           
            
    
