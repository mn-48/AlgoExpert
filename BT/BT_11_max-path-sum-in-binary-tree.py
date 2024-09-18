# # O(n) Time | O(log(n)) Space

# def maxPathSum(tree):
#     # Write your code here.
#     maxSum = [tree.value]

#     def dfs(tree):
#         if tree is None:
#             return 0
#         left = dfs(tree.left)
#         right = dfs(tree.right)

#         maxSum[0] = max(maxSum[0], tree.value+right+left, tree.value+right, tree.value+left)

#         return tree.value+max(left, right)
#     dfs(tree)

#     return maxSum[0]


# O(n) time | O(log(n)) Space

def maxPathSum(tree):
    _, maxSum = findMaxSum(tree)
    return maxSum


def findMaxSum(tree):
    if tree is None:
        return (0, float("-inf"))

    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch + value, value)
    maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch) 
    maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)
    return (maxSumAsBranch, maxPathSum)