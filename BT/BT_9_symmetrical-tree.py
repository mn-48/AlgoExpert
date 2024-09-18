# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Recursive solution ========================================== 
# O(n) Time | O(h) Space
def symmetricalTree(tree):
    return isSymmetricalTree(tree.left, tree.right)

def isSymmetricalTree(tree1, tree2):
    if tree1 is not None and tree2 is not None and tree1.value == tree2.value:
           return  isSymmetricalTree(tree1.left, tree2.right) and isSymmetricalTree(tree1.right, tree2.left)
    return tree1==tree2
    

# Iterative solution ========================================== 
# O(n) Time | O(h) Space
def symmetricalTree(tree):
    stackLeft = [tree.left]
    stackRight = [tree.right]

    while len(stackLeft) > 0:
        left = stackLeft.pop()
        right = stackRight.pop()

        if left is None and right is None:
            continue

        if left is None or right is None or left.value != right.value:
            return False

        stackLeft.append(left.left)
        stackLeft.append(left.right)
        stackRight.append(right.right)
        stackRight.append(right.left)

    return True

