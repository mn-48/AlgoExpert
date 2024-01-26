# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# # O(n) Time | O(n) Space
# def findSuccessor(tree, node):
#     inOrderTraversalOrder = getInOrderTraversalOrder(tree)
#     for idx, currenrNode in enumerate(inOrderTraversalOrder):
#         if currenrNode != node:
#             continue
#         if idx == len(inOrderTraversalOrder)-1:
#             return None
        
#         return inOrderTraversalOrder[idx+1]

# def getInOrderTraversalOrder(node, order=[]):
#     if node is None:
#         return order 
    
#     getInOrderTraversalOrder(node.left, order)
#     order.append(node)
#     getInOrderTraversalOrder(node.right, order)
#     return order


# # O(h) Time | O(1) Space
def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftmostChild(node)
    return getRightmostParent(node)

def getLeftmostChild(node):
    currentNode = node.right
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode

def getRightmostParent(node):
    currentNode = node
    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent
    return currentNode.parent




# root = BinaryTree(1)
# root.left = BinaryTree(2)
# root.left.parent = root
# root.right = BinaryTree(3)
# root.right.parent = root
# root.left.left = BinaryTree(4)
# root.left.left.parent = root.left
# root.left.right = BinaryTree(5)
# root.left.right.parent = root.left
# root.left.left.left = BinaryTree(6)
# node = root.left.right


# res = findSuccessor(root, node)
# # print(res.value)


