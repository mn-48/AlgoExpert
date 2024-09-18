# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) Time | o(h) Space
def splitBinaryTree(tree):
    subsums = set()
    total = getTotal(tree, subsums)
    return total/2 if total/2 in subsums else 0
    
def getTotal(tree, subsums):
    if not tree:
        return 0
    total = getTotal(tree.left, subsums)+getTotal(tree.right, subsums)+tree.value
    subsums.add(total)
    
    return total
    