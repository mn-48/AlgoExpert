# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(m+n) time | o(max(h1, h2)) Space
def compareLeafTraversal(tree1, tree2):
    array1 = []
    array2 = []
    arrayOfLeaves(tree1, array1)
    arrayOfLeaves(tree2, array2)
    # Write your code here.
    if array1==array2:
        return True
    else:
        return False

def arrayOfLeaves(tree, array):
    if tree is None:
        return
    arrayOfLeaves(tree.left, array)
    if tree.left is None and tree.right is None:
        array.append(tree.value)
    arrayOfLeaves(tree.right, array)

