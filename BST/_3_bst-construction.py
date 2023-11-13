# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average o(log(n)) Time | O(1) Space
    # Wrost o(n) Time | O(1) Space
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
                    
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # Average o(log(n)) Time | O(1) Space
    # Wrost o(n) Time | O(1) Space
    def contains(self, value):
        currentNode = self

        while currentNode is not None:
            if currentNode.value == value:
                return True
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
            
        return False

    # Average o(log(n)) Time | O(1) Space
    # Wrost o(n) Time | O(1) Space
    def remove(self, value, parentNode=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        parentNode, node = self.GetFirst(value, parentNode)

        if node is None:
            return

        if self.IsOnlyNode(parentNode, node):
            return 
        
        if node.left and node.right:
            repNode = node.right.GetMinNode(parentNode)
            node.value = repNode.value
            node.right.remove(repNode.value, node)

        elif node.left is None and node.right is None:
            if parentNode.left == node:
                parentNode.left = None
            elif parentNode.right == node:
                parentNode.right = None
        elif node.left:
            repNode = node.left.GetMaxNode(parentNode)
            node.value = repNode.value
            node.left.remove(repNode.value, node)

        elif node.right:
            repNode = node.right.GetMinNode(parentNode)
            node.value = repNode.value
            node.right.remove(repNode.value, node)
        
        
        
        return self
    
    def IsOnlyNode(self, parentNode, node):
        return parentNode is None and node.left is None and node.right is None
    
    def GetFirst(self, value, parentNode=None):
        node = self

        while node is not None:
            if value == node.value:
                return parentNode, node
            elif value < node.value:
                parentNode = node
                node = node.left
            else:
                parentNode = node
                node = node.right
        return None, None
    
    def GetMinNode(self, parentNode):
        node = self
        while node.left:
            parentNode = node
            node = node.left
        return node
    
    def GetMaxNode(self, parentNode):
        node = self
        while node.right:
            parentNode = node
            node = node.max 
        return node


    # def remove(self, value, parentNode = None):
    #     currentNode = self
    #     while currentNode is not None:
    #         if value < currentNode.value:
    #             parentNode = currentNode
    #             currentNode = currentNode.left
    #         elif value > currentNode.value:
    #             parentNode = currentNode
    #             currentNode = currentNode.right
    #         else:
    #             if currentNode.left is not None and currentNode.right is not None:
    #                 currentNode.value = currentNode.right.getMinValue()
    #                 currentNode.right.remove(currentNode.value, currentNode)
    #             elif parentNode is None:
    #                 if currentNode.left is not None:
    #                     currentNode.value = currentNode.left.value
    #                     currentNode.right = currentNode.left.right
    #                     currentNode.left = currentNode.left.left
    #                 elif currentNode.right is not None:
    #                     currentNode.value = currentNode.right.value
    #                     currentNode.left = currentNode.right.left
    #                     currentNode.right = currentNode.right.right
    #                 else:
    #                     currentNode.value = None
    #             elif parentNode.left == currentNode:
    #                 parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
    #             elif parentNode.right==currentNode:
    #                 parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
    #             break
    #     return self
    
    # def getMinValue(self):
    #     currentNode = self
    #     while currentNode.left is not None:
    #         currentNode = currentNode.left
    #     return currentNode.value
