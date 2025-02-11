
# O(d*(n+b)) Time | O(n+b) space
def radixSort(array):
    if len(array) == 0:
        return array
    maxNumber = max(array)
    digit = 0
    while maxNumber / 10 ** digit > 0:
        countingSort(array, digit)
        digit += 1
    return array


def countingSort(array, digit):
    sortedArray = [0] * len(array)
    countArray = [0] * 10

    digitColumn = 10**digit

    for num in array:
        countIndex = (num // digitColumn) % 10
        countArray[countIndex] += 1
    for idx in range(1, 10):
        countArray[idx] += countArray[idx-1]

    for idx in range(len(array)-1, -1, -1):
        countIndex = (array[idx]//digitColumn) % 10
        countArray[countIndex] -= 1
        sortedIndex = countArray[countIndex]
        sortedArray[sortedIndex] = array[idx]

    for idx in range(len(array)):
        array[idx] = sortedArray[idx]
