# O(n^2) Time O(n) Space

def bubbleSort(array):
    isSorted = False
    cnt = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1-cnt):
            if array[i] > array[i+1]:
                array[i], array[i+1] =  array[i+1], array[i]
                isSorted = False
        cnt+=1
    return array
    
