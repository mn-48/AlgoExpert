# O(n) Time | O(h) space
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx


def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float('-inf'), float('inf'), preOrderTraversalValues, treeInfo)

def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, currentSubTreeInfo):

    if currentSubTreeInfo.rootIdx == len(preOrderTraversalValues):
        return None
    
    rootValue = preOrderTraversalValues[currentSubTreeInfo.rootIdx]

    if rootValue < lowerBound or rootValue >= upperBound:
        return None
    currentSubTreeInfo.rootIdx += 1
    leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, currentSubTreeInfo)
    rightSubtree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, currentSubTreeInfo)
    return BST(rootValue, leftSubtree, rightSubtree)

