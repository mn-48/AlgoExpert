
# In pseudocode, it's roughly this:
# 1. Start at the root node.
# 2. If currentNode has no left child, then process it and move to its right child.
# 3. If currentNode does have a left child, find the rightmost node of this left child (we'll call it "predecessor"). Two situations can happen here:
#   3.1(a) If predecessor has no right child, we make its right child point to currentNode. This creates a temporary link back to currentNode. We then move to the currentNode's left child.
#   3.2(b) If the predecessor has a right child, this means it's a link we made before. So, we process currentNode, break the link (set predecessor's right child back to None), and move to the currentNode's right child.
# 4 Repeat the above process until we've visited all the nodes.



# class BST:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right


# # O(n) Time | O(1) Space 
# def repairBst(tree):
#     # Write your code here.
#     nodeOne, nodeTwo, previousNode = None
#     currentNode = tree

#     def processNode():
#         nonlocal nodeOne, nodeTwo, previousNode, currentNode
#         if previousNode is not None and previousNode.value > currentNode.value:
#             if nodeOne is None:
#                 nodeOne = previousNode
#             nodeTwo = currentNode
#         previousNode = currentNode
#         currentNode = currentNode.right

#     while currentNode is not None:
#         if currentNode.left is None:
#             processNode()
#         else:
#             predecessor = currentNode.left

#             while predecessor.right is not None and predecessor.right != currentNode:
#                 predecessor = predecessor.right
#             if predecessor.right is None:
#                 predecessor.right = currentNode
#                 currentNode = currentNode.left
#             else:
#                 processNode()
#                 predecessor.right = None

#     nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value
#     return tree

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) Time | O(h) Space
def repairBst(tree):
    nodeOne= None
    nodeTwo=None
    previousNode = None
    stack = []
    
    currentNode = tree

    while currentNode is not None or len(stack) > 0:
        while currentNode is not None:
            stack.append(currentNode)
            currentNode = currentNode.left
        currentNode = stack.pop()

        if previousNode is not None and previousNode.value > currentNode.value:
            if nodeOne is None:
                nodeOne = previousNode
            nodeTwo= currentNode
        previousNode = currentNode
        currentNode = currentNode.right

    nodeOne.value, nodeTwo.value = nodeTwo.value, nodeOne.value
    return tree
