# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) Time | O(h) Space
def symmetricalTree(tree):
    return isSymmetricalTree(tree.left, tree.right)

def isSymmetricalTree(tree1, tree2):
    if tree1 is not None and tree2 is not None and tree1.value == tree2.value:
           return  isSymmetricalTree(tree1.left, tree2.right) and isSymmetricalTree(tree1.right, tree2.left)
    return tree1==tree2
    