# #Time O(n^2)  | Space O(1)
# def twoNumberSum(array, targetSum):
#     # Write your code here.
#     n = len(array)
#     for i in range(n-1):
#         for j in range(i+1, n):
#             if array[i]+array[j] == targetSum:
#                 return [array[i] , array[j]]
#     return []


# #  O(n) Time | O(n) Space

# def twoNumberSum(array, targetSum):
#     nums = {}
#     for x in array:
#         y = targetSum-x
#         if y in nums:
#             return [x, y]
#         else:
#             nums[x] = True
#     return []


#  O(nlog(n)) Time | O(1) Space

def twoNumberSum(array, targetSum):
    array.sort()

    left = 0
    right = len(array)-1

    while left < right:
        if array[left] + array[right] == targetSum:
            return [array[left], array[right]]
        elif array[left] + array[right] > targetSum:
            right -= 1
        elif array[left] + array[right] < targetSum:
            left += 1
    return []


if __name__ == "__main__":
    ans = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
    print(ans)
