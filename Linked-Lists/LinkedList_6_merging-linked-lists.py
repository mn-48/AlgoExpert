# # This is an input class. Do not edit.
# class LinkedList:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# # O(m+n) Time | O(n) Space
# def mergingLinkedLists(linkedListOne, linkedListTwo):

#     listOneNodes = set()
#     currentNodeOne = linkedListOne
#     while currentNodeOne is not None:
#         listOneNodes.add(currentNodeOne)
#         currentNodeOne = currentNodeOne.next
        
#     currentNodeTwo = linkedListTwo
#     while currentNodeTwo is not None:
#         if currentNodeTwo in listOneNodes:
#             return currentNodeTwo
#         currentNodeTwo = currentNodeTwo.next
#     return None


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(m+n)  Time | O(1) Space
def mergingLinkedLists(linkedListOne, linkedListTwo):
    currentNodeOne = linkedListOne
    currentNodeTwo = linkedListTwo

    while currentNodeOne is not currentNodeTwo:
        if not currentNodeOne:
            currentNodeOne = linkedListTwo
        else:
            currentNodeOne = currentNodeOne.next
            
        if not currentNodeTwo:
            currentNodeTwo = linkedListOne
        else:
            currentNodeTwo = currentNodeTwo.next
    # Write your code here.
    return currentNodeOne
