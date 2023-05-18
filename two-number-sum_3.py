# *Time O(n) Space O(n)*

def twoNumberSum(array, targetSum):
    # Write your code here.
    nums = {}

    for x in array:
        y = targetSum-x

        if y in nums:
            return [x, y]
        else:
            nums[x] = True

    return []

