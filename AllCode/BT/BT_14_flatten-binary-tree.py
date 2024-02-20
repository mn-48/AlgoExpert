# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# O(n) Time | O(d) Space
def flattenBinaryTree(root, head=None):
    if not root:
        return head
    head = flattenBinaryTree(root.right, head)
    root.right = head
    if head:
        head.left = root
    head = root
    return  flattenBinaryTree(root.left, head)
   
