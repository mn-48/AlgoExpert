def findClosestValueInBst(tree, target):
    return helperFindClosestValueInBst(tree, target, closest = float("inf"))

def helperFindClosestValueInBst(tree, target, closest):
    
    current_node = tree
    
    
    while current_node is not None:
        if  abs(target-closest) > abs(target-current_node.value) :
            closest = current_node.value
        if target > current_node.value:
            current_node = current_node.right
        elif target < current_node.value:
            current_node = current_node.left
        else:
            break
    return closest
    
 

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



if __name__=="__main__":

    """
    tree  =     10
            /    \
            5      15
            /  \   /   \
        2   5  13    22
        /         \14
        1

    """

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

    target = 12   
    print(findClosestValueInBst(root, target))