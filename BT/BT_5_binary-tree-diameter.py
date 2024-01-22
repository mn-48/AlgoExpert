# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

# Time O(n) | Space O(h)
def binaryTreeDiameter(tree):
    # Write your code here.
    return getBinaryTreeInfo(tree).diameter


def getBinaryTreeInfo(tree):
    if tree is None:
        return BinaryTreeInfo(0, 0)

    leftTreeInfo = getBinaryTreeInfo(tree.left) 
    rightTreeInfo = getBinaryTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)

    currentDiameter = max(longestPathThroughRoot, maxDiameterSoFar)
    currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return BinaryTreeInfo(currentDiameter, currentHeight)


