# O(h) time | O(1) Space
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    return ( isChild(nodeOne, nodeTwo) and isChild(nodeTwo, nodeThree)) or (isChild(nodeThree, nodeTwo) and isChild(nodeTwo, nodeOne))

def isChild(node, child):
    while node is not None and node is not child:
        node = node.left if child.value < node.value else node.right
    return node is child
    
 