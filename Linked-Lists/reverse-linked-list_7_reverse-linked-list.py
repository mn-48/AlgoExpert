# # This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# # O(n) Time | O(1) Space
# def reverseLinkedList(head):
#     previousNode, currentNode = None, head

#     while currentNode is not None:
#         nextNode = currentNode.next
#         currentNode.next = previousNode
#         previousNode = currentNode
#         currentNode = nextNode
#     return previousNode
        
        
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) Time | O(1) Space
def reverseLinkedList(head):
    p1, p2 = None, head

    while p2 is not None:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
        
    return p1
