# # O(nlog(n)) Time | O(1) Space
# def quickselect(array, k):
#     array.sort()
#     return array[k-1]

# O(nlog(n)) Time | O(1) Space
def quickselect(array, k):
    return quickselectHelper(array, 0, len(array) - 1, k - 1)


def quickselectHelper(array, startIdx, endIdx, position):
    while True:
        if startIdx > endIdx:
            raise Exception("Your algorithm should never arrive here!")
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        while leftIdx <= rightIdx:
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                swap(leftIdx, rightIdx, array)
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
        swap(pivotIdx, rightIdx, array)
        if rightIdx == position:
            return array[rightIdx]
        elif rightIdx < position:
            startIdx = rightIdx + 1
        else:
            endIdx = rightIdx - 1


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    ans = quickselect([8, 5, 2, 9, 7, 6, 3], 3)
    print(ans)
