
# inOrder = [1, 2, 5, 5, 10, 15, 22]
# preOrder = [10, 5, 2, 1, 5, 15, 22]
# postOrder = [1, 2, 5, 5, 22, 15, 10]

# O(N) Time | O(N) Space
def inOrderTraverse(tree, array):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


# O(N) Time | O(N) Space
def preOrderTraverse(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


# O(N) Time | O(N) Space
def postOrderTraverse(tree, array):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array
