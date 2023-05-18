# *Time O(nlog(n)) Space O(1) with binary search*

def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()

    n = len(array)
    left = 0
    right = n-1

    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]
        elif array[left] + array[right] > targetSum:
            right -= 1 
        elif array[left] + array[right] < targetSum:
            left += 1 
    return []

