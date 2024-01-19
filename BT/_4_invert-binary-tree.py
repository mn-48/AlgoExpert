# O(n) Time | O(h) Space
def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
        return
    invertBinaryTree(tree.left) 
    invertBinaryTree(tree.right)
    tree.left, tree.right = tree.right, tree.left
    


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
