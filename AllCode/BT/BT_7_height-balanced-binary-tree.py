# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height
        
# O(n) Time | O(1) Space

def heightBalancedBinaryTree(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced

def getTreeInfo(node):
    if node is None:
        return TreeInfo(True, -1)
    
    leftSubtreeInfo = getTreeInfo(node.left)
    rightSubtreeInfo = getTreeInfo(node.right)

    isBalanced = leftSubtreeInfo.isBalanced and rightSubtreeInfo.isBalanced and abs(leftSubtreeInfo.height - rightSubtreeInfo.height)<=1
    height = max(leftSubtreeInfo.height, rightSubtreeInfo.height)+1
    return TreeInfo(isBalanced, height)