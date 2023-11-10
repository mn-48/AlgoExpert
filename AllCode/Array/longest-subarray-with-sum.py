# O(n) Time | O(1) Space
def longestSubarrayWithSum(array, targetSum):
    # Write your code here.
    indeces = []
    
    left, right = 0,0
    curr_sum = 0
    while right<len(array):
        curr_sum += array[right]

        while left < right and curr_sum > targetSum:
            curr_sum -= array[left]
            left +=1

        if curr_sum == targetSum:
            if len(indeces)==0 or indeces[1]-indeces[0]< right-left:
                indeces = [left, right]
        right += 1
    return indeces
            