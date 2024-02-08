# O(n) Time | O(1) Space

def iterativeInOrderTraversal(tree, callback):
    # Write your code here
    stack = []
    while len(stack) or tree is not None:
        while tree is not None:
            stack.append(tree)
            tree = tree.left
        tree = stack.pop()
        callback(tree)
        tree = tree.right
    return