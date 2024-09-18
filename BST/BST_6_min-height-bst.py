def minHeightBst(array):
    left = 0
    right = len(array)-1
    mid = (left+right)//2
    if left > right:
        return 

    node = BST(array[mid])
    node.left = minHeightBst(array[:mid])
    node.right = minHeightBst(array[mid+1:])

    return node



class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
