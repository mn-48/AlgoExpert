# # O(n) Time | O(1) Space

# def iterativeInOrderTraversal(tree, callback):
#     # Write your code here
#     stack = []
#     while len(stack) or tree is not None:
#         while tree is not None:
#             stack.append(tree)
#             tree = tree.left
#         tree = stack.pop()
#         callback(tree)
#         tree = tree.right
#     return


# O(n) Time | O(1) Space

def iterativeInOrderTraversal(tree, callback):
    previousNode = None
    currentNode = tree

    while currentNode is not None:
        if previousNode is None or previousNode==currentNode.parent:
            if currentNode.left is not None:
                nextNode = currentNode.left
            else:
                callback(currentNode)
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
               
        elif previousNode == currentNode.left:
            callback(currentNode)
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        else:
            nextNode = currentNode.parent
        previousNode = currentNode
        currentNode = nextNode

