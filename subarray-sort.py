# O(n) Time | O(1) Space
 
def subarraySort(array):
    left , right = -1, -1

    max_val, min_val = array[0], array[-1]

    for i, el in enumerate(array):
        if el < max_val:
            left = i
        else:
            max_val = el
            

    for i, el in reversed(list(enumerate(array))):
        if el > min_val:
            right = i
        else:
            min_val = el
    return [right, left]


# array = [1,2,4,7,10,11,7,12,6,7,16,18,19]
# ans = subarraySort(array)

# print(ans)