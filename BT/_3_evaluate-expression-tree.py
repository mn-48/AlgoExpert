# This is an input class. Do not edit.

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) Time | O(h) Space
def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value 
    leftValue = evaluateExpressionTree(tree.left)
    rightValue = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return leftValue + rightValue

    if tree.value == -2:
        return leftValue - rightValue

    if tree.value == -3:
        return int(leftValue / rightValue)
    
    return leftValue * rightValue

