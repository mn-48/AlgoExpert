# Time O(nlog(n)+mlog(m)) | space O(1)

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    i , j = 0, 0

    smallest = float('inf')
    pair = []

    while i < len(arrayOne) and j < len(arrayTwo):
        n1 = arrayOne[i]
        n2 = arrayTwo[j]
        current = abs(n1- n2)

        if current < smallest:
            smallest = current
            pair = [n1, n2]
        if n1 > n2:
            j+=1
        else:
            i+=1
    return pair
            
        
    