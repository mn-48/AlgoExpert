"""
tree  =     10
          /    \
         5      15
        /  \   /   \
       2   5  13    22
      /         \14
     1

"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
# tree
root = BST(10)
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)
