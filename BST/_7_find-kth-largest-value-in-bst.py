# This is an input class. Do not edit.
# O(h+k) Time| O(k) space
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, numberOfVisitedNode, lastVisitedNodeValue):
        self.numberOfVisitedNode = numberOfVisitedNode
        self.lastVisitedNodeValue = lastVisitedNodeValue


def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraverse(tree, k, treeInfo)
    return treeInfo.lastVisitedNodeValue

def reverseInOrderTraverse(node, k, treeInfo):
    if node == None or  treeInfo.numberOfVisitedNode >= k:
        return
    reverseInOrderTraverse(node.right, k, treeInfo)
    if treeInfo.numberOfVisitedNode < k:
        treeInfo.numberOfVisitedNode += 1
        treeInfo.lastVisitedNodeValue = node.value
        reverseInOrderTraverse(node.left, k, treeInfo)

    
