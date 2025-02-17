# best, worse, average 
# O(nlog(n)) Time | O(nlog(n)) Space

def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array)//2

    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]

    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))


def mergeSortedArrays(leftHalf, rightHalf):
    sortedArrays = [None] * (len(leftHalf) + len(rightHalf))
    k = i = j = 0
    while i< len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArrays[k] = leftHalf[i]
            i+=1
        else:
            sortedArrays[k] = rightHalf[j]
            j+=1
        k+=1
    while i< len(leftHalf):
        sortedArrays[k] = leftHalf[i]
        i+=1
        k+=1
        
    while j < len(rightHalf):
        sortedArrays[k] = rightHalf[j]
        j+=1
        k+=1
    return sortedArrays
        