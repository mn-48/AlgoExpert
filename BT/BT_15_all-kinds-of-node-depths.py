
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# # Iterative Solution ==========================
# # O(nlog(n)) Time | O(h) Space 
# def allKindsOfNodeDepths(root):
#     sumOfAllDepths = 0
#     stack = [root]

#     while len(stack) > 0:
#         node = stack.pop()
#         if node is None:
#             continue
#         sumOfAllDepths += nodeDepths(node)
#         stack.append(node.left)
#         stack.append(node.right)
#     return sumOfAllDepths


# Recursive Solution ======================= 
# O(nlog(n)) Time | O(h) Space  

# def allKindsOfNodeDepths(root):
#     if root is None:
#         return 0
#     # Write your code here.
#     return allKindsOfNodeDepths(root.left)+allKindsOfNodeDepths(root.right)+nodeDepths(root)

# def nodeDepths(node, depth=0):
#     if node is None:
#         return 0
#     return depth + nodeDepths(node.left, depth+1) + nodeDepths(node.right, depth+1)

# #  solve with touple ===========================
# # O(n) Time | O(d) Space
# def allKindsOfNodeDepths(root):
#     sum_all = 0
#     stack = []
#     current, depth, depth_sum = root, 0, 0

#     while True:
#         if current:
#             depth_sum += depth
#             sum_all += depth_sum
#             stack.append((current, depth, depth_sum))
#             current, depth = current.left, depth+1
#         elif stack:
#             popped, depth, depth_sum = stack.pop()
#             current, depth = popped.right, depth+1
#         else:
#             break
            
#     return sum_all


#  official solve  ===========================
# O(n) Time | O(d) Space

def allKindsOfNodeDepths(root):
    return getTreeInfo(root).sumOfAllDepths

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0, 0)
    
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    sumOfLeftDepths = leftTreeInfo.sumOfDepths + leftTreeInfo.numNodesInTree
    sumOfRightDepths = rightTreeInfo.sumOfDepths + rightTreeInfo.numNodesInTree

    numNodesInTree = 1 + leftTreeInfo.numNodesInTree+ rightTreeInfo.numNodesInTree
    sumOfDepths = sumOfLeftDepths + sumOfRightDepths
    sumOfAllDepths = sumOfDepths+leftTreeInfo.sumOfAllDepths +rightTreeInfo.sumOfAllDepths

    return TreeInfo(numNodesInTree, sumOfDepths, sumOfAllDepths)
    


class TreeInfo:
    def __init__(self, numNodesInTree, sumOfDepths, sumOfAllDepths):
        self.numNodesInTree = numNodesInTree
        self.sumOfDepths = sumOfDepths
        self.sumOfAllDepths = sumOfAllDepths